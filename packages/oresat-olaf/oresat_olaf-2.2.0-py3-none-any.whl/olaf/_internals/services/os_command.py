import subprocess
from enum import IntEnum

from loguru import logger

from ...common.service import Service


class OSCommandState(IntEnum):
    NO_ERROR_NO_REPLY = 0x00
    NO_ERROR_REPLY = 0x01
    ERROR_NO_REPLY = 0x02
    ERROR_REPLY = 0x03
    EXECUTING = 0xFF


class OSCommandService(Service):
    '''Service for running OS (bash) commands over CAN bus as defined by CiA 301 specs'''

    def __init__(self):
        super().__init__()

        self.index = 0x1023
        self.sub_command = 0x01
        self.sub_state = 0x02
        self.sub_reply = 0x03

        self.command = ''
        self.state = OSCommandState.NO_ERROR_NO_REPLY
        self.reply = ''
        self.reply_max_len = 10000
        self.failed = False

    def on_start(self):

        self.node.add_sdo_read_callback(self.index, self.on_read)
        self.node.add_sdo_write_callback(self.index, self.on_write)

    def on_loop(self):

        if self.state == OSCommandState.EXECUTING:
            logger.info('Running OS command: ' + self.command)

            out = subprocess.run(self.command, capture_output=True, shell=True)
            if out.returncode != 0:  # error
                self.reply = out.stderr[:self.reply_max_len].decode()
                if self.reply:
                    self.state = OSCommandState.ERROR_REPLY
                else:
                    self.state = OSCommandState.ERROR_NO_REPLY
            else:  # no error
                self.reply = out.stdout[:self.reply_max_len].decode()
                if self.reply:
                    self.state = OSCommandState.NO_ERROR_REPLY
                else:
                    self.state = OSCommandState.NO_ERROR_NO_REPLY

            logger.info('OS command has completed')

        self.sleep(0.5)

    def on_loop_error(self, exc: Exception):

        self.failed = True
        self.command = ''
        self.state = OSCommandState.ERROR_NO_REPLY
        self.reply = ''
        logger.exception(exc)

    def on_read(self, index: int, subindex: int):

        ret = None

        if index == self.index and not self.failed:
            if subindex == self.sub_command:
                ret = self.command.encode()
            elif subindex == self.sub_state:
                ret = self.state.value
            elif subindex == self.sub_reply:
                ret = self.reply.encode()

        return ret

    def on_write(self, index: int, subindex: int, value):

        if index == self.index and subindex == self.sub_command:
            if self.state == OSCommandState.EXECUTING or self.failed:
                logger.eror('cannot start another os command when one is running')
                return

            self.reply = ''
            self.command = value.decode()
            self.state = OSCommandState.EXECUTING  # run os command
