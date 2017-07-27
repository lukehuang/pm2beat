from pm2beat import BaseTest

import os


class Test(BaseTest):

    def test_base(self):
        """
        Basic test with exiting Pm2beat normally
        """
        self.render_config_template(
                path=os.path.abspath(self.working_dir) + "/log/*"
        )

        pm2beat_proc = self.start_beat()
        self.wait_until( lambda: self.log_contains("pm2beat is running"))
        exit_code = pm2beat_proc.kill_and_wait()
        assert exit_code == 0
