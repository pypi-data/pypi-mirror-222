import finesse
from finesse.analysis.actions import FrequencyResponse, For
import numpy as np


def test_symbolic_dof_amplitude():
    model = finesse.script.parse(
        """
    var Y 1
    l l1
    readout_dc PD
    link(l1, PD)
    dof INT l1.dofs.amp Y
    fsig(1)
    """
    )

    values = [1, 2, 3, 4, 5]
    out = model.run(
        For(
            model.Y.value,
            values,
            FrequencyResponse([1], [model.INT.AC.i], [model.PD.DC.o]),
        )
    )

    result = [complex(sol.out.squeeze()) for sol in out.children]
    assert np.allclose(values, result)
