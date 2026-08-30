from __future__ import annotations

import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class RepositoryContractTests(unittest.TestCase):
    def test_release_version_starts_at_1_0_0(self) -> None:
        project = (ROOT / ".hemtt" / "project.toml").read_text(encoding="utf-8")
        self.assertIn("major = 1", project)
        self.assertIn("minor = 0", project)
        self.assertIn("patch = 0", project)

    def test_every_addon_has_a_legacy_pboprefix(self) -> None:
        addon_dirs = [
            path
            for root_name in ("addons", "optionals")
            for path in (ROOT / root_name).glob("*")
            if path.is_dir()
        ]
        self.assertTrue(addon_dirs)
        for addon_dir in addon_dirs:
            with self.subTest(addon=addon_dir.name):
                prefix = addon_dir / "$PBOPREFIX$"
                self.assertTrue(prefix.is_file())
                self.assertTrue(prefix.read_text(encoding="utf-8").strip())

    def test_fiber_stabilization_import_is_present(self) -> None:
        functions = ROOT / "addons" / "vnd_main" / "functions"
        for name in (
            "fn_fpv_applyGravity.sqf",
            "fn_fpv_fiberTick.sqf",
            "fn_fpv_syncPath.sqf",
            "fn_fpv_updateFiberPath.sqf",
        ):
            with self.subTest(function=name):
                self.assertTrue((functions / name).is_file())

    def test_waypoint_ai_is_not_fully_disabled(self) -> None:
        drone_init = (
            ROOT / "addons" / "vnd_main" / "functions" / "fn_fpv_droneInit.sqf"
        ).read_text(encoding="utf-8")
        self.assertNotIn('disableAI "ALL"', drone_init)


if __name__ == "__main__":
    unittest.main()
