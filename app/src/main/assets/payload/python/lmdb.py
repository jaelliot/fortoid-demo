"""LMDB placeholder shim for Pyodide payloads using IndexedDB persistence."""

class Error(Exception):
    """Compatibility exception type for code importing lmdb.Error."""


def open(*_args, **_kwargs):
    raise Error("lmdb shim: persistent storage is provided by indexeddb_python")
