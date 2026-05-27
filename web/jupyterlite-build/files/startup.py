# Kernel startup hook for the in-browser Pyodide kernel.
#
# Runs once when a new kernel session begins. Installs the qcsim wheel
# (which mirrors the braket.* namespace) so notebook code written as
# `from braket.circuits import Circuit` works unchanged. Also extends
# sys.path so `from lib.utils.results import ...` resolves against the
# curriculum's shared library.

import sys

try:
    import piplite
    await piplite.install(["/files/wheels/qcsim-0.1.0-py3-none-any.whl"])  # noqa: F704
except Exception as exc:  # pragma: no cover - kernel diagnostic only
    print(f"[startup] piplite install failed: {exc}", file=sys.stderr)

# Trigger the braket.* alias registration in qcsim/__init__.py.
import qcsim  # noqa: F401, E402

# Make the curriculum's `lib/` importable.
if "/files" not in sys.path:
    sys.path.insert(0, "/files")
