import pytest


@pytest.mark.cupy
def test_main():
    from pySDC.projects.GPU.ac_fft import main

    main()
