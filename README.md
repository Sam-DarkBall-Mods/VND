# VND

[![CI](https://github.com/Sam-DarkBall-Mods/VND/actions/workflows/ci.yml/badge.svg)](https://github.com/Sam-DarkBall-Mods/VND/actions/workflows/ci.yml)

VND adds KVN fiber optic FPV drones. AT and AP versions are available for all
three sides, with normal and thermal variants. The fiber path is updated during
flight, synchronized in multiplayer and can remain visible for a configurable
time after the drone is destroyed.

The mod also contains the FPV display, inventory packing and the connection
logic used when the operator takes or releases control.

## Requirements

- Arma 3 2.22 or newer
- CBA_A3

## Building

```bash
python3 -B -m unittest discover -s tests -p "test_*.py" -v
hemtt check
hemtt build --no-bin
```

The release stays compatible with the `vnd_main` prefix and existing KVN
class names.

## License

Code and configs use GPL-2.0-or-later. Original models, textures, materials,
animations and audio use APL-SA. See [LICENSES.md](LICENSES.md).
