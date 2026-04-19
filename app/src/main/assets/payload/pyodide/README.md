## Pyodide 0.29.1

This directory is the local Pyodide cache used by the Fort-ios proof-harness lane and the Fort-ios payload build pipeline.

Core runtime files in this directory come from the official Pyodide CDN or release assets for version `0.29.1`, as downloaded by [scripts/download-pyodide.sh](libs/Fort-ios/scripts/download-pyodide.sh).

Important distinction:

- This directory is **not** the FortWeb browser lane's vendored runtime.
- FortWeb currently carries its own bundled runtime under `libs/fortweb/vendor/pyodide/0.29.3/`.
- When the iOS wrapper hosts FortWeb through `PAYLOAD_SOURCE=fortweb`, that hosted payload uses FortWeb's vendored runtime, not the files in this directory.

When bumping the Fort-ios local runtime later:

1. Update the pinned version in [scripts/download-pyodide.sh](libs/Fort-ios/scripts/download-pyodide.sh).
2. Keep [src/constants.ts](libs/Fort-ios/src/constants.ts) in sync with the same Pyodide version.
3. Refresh any wheel filenames whose tags depend on the Pyodide or Python version.
4. Re-run the local proof-harness checks that depend on this runtime.
