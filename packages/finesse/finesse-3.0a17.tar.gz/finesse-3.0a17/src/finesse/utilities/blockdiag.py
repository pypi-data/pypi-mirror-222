import sys
import io
import re

from finesse.components.node import NodeType


def get_loops_blockdiag_code(model, f=sys.stdout, remove_mechanical_to_mechanical=True):
    from finesse.components.node import SignalNode
    from copy import deepcopy
    import networkx as nx

    re1 = re.compile(
        "(?P<sum>__sum_)*(?:__(?P<optics_dir>in|out)_optics_)*(?P<name>.*)"
    )
    signal_network = model.network.copy()
    for node in deepcopy(signal_network.nodes):
        N = model.get(node)
        if not isinstance(N, SignalNode):
            signal_network.remove_node(node)

    signal_network.remove_nodes_from(list(nx.isolates(signal_network)))

    # remove mechanical to mechanical couplings as there are many
    # and are complicated to look at anyway
    if remove_mechanical_to_mechanical:
        for i, o in deepcopy(signal_network.edges):
            if (
                model.get(i).type == NodeType.MECHANICAL
                and model.get(i).type == NodeType.MECHANICAL
            ):
                signal_network.remove_edge(i, o)

    mapping = {}
    for i, o in deepcopy(signal_network.edges):
        I = model.get(i)
        O = model.get(o)
        if I.component is O.component and I.type == O.type == NodeType.ELECTRICAL:
            net = signal_network = nx.contracted_nodes(
                signal_network, i, o, self_loops=False
            )
            mapping[i] = I.component.name

    signal_network = nx.relabel_nodes(signal_network, mapping)
    signal_network.remove_nodes_from(list(nx.isolates(signal_network)))
    net = signal_network

    print("blockdiag {", file=f)
    print("default_shape = box;", file=f)
    for n in net.nodes:
        res = re1.match(n).groupdict()
        if res is None:
            raise Exception(f"Unexpected {n}")
        if res["sum"] is not None:
            print(f"{n} [shape = circle , label='+', width=20, height=20];", file=f)
        elif res["optics_dir"] == "out":
            print(f"{n} [shape = beginpoint, label = '{res['name']}'];", file=f)
        elif res["optics_dir"] == "in":
            print(f"{n} [shape = endpoint, label = '{res['name']}'];", file=f)
        else:
            print(f"{n} [label = '{res['name']}'];", file=f)

    for i, o in signal_network.edges():
        print(f"{i} -> {o};", file=f)

    print("}", file=f)


def display_blockdiag_output(cell, output_format="svg", return_svg=False):
    """When called in a Jupyter/Ipython environment the block diagram is displayed.

    Parameters
    ----------
    output_format : str
        svg or png
    return_svg : bool
        Returns SVG data if requested
    """
    import tempfile
    import blockdiag.command
    from IPython.core.displaypub import publish_display_data

    command = blockdiag.command
    mime_type = {
        "png": "image/png",
        "svg": "image/svg+xml",
    }

    with tempfile.NamedTemporaryFile(suffix=".diag", delete=False) as f:
        cell += "\n"
        f.write(cell.encode("utf-8"))
        f.flush()
        with tempfile.NamedTemporaryFile(suffix="." + output_format, delete=False) as p:
            args = [f"-T{output_format}", "-o", p.name, f.name]
            command.main(args=args)
            p.seek(0)
            data = p.read()

            if output_format in ["svg"]:
                data = data.decode("utf-8")

            publish_display_data({mime_type.get(output_format, "text/plain"): data})

    if return_svg:
        return data


def display_loops_blockdiag(model, remove_mechanical_to_mechanical=True, **kwargs):
    """Displays a block diagram of a model using the `blockdiag` package. Only signal
    path (electronic and mechanical) connections are shown.

    Parameters
    ----------
    model : :class:`Model`
        Model to display
    remove_mechanical_to_mechanical : bool, optional
        If true, mechanical to mechanical node edges
    **kwargs
        options to pass to :function:`get_loops_blockdiag_code`.

    Returns
    -------
    Nothing if return_svg=False
    """
    f = io.StringIO()
    get_loops_blockdiag_code(
        model, f, remove_mechanical_to_mechanical=remove_mechanical_to_mechanical
    )
    return display_blockdiag_output(f.getvalue(), **kwargs)
