import logging

import command


class Command_EVAL_CLIENT(command.ClientCommand):
    """ eval called client side. Use with care. """

    def on_init(self, args):
        """ server side """
        logging.debug("    CS on_init")

    def on_answer(self, success, answer):
        """ server side """
        logging.debug("    CS on_answer")

    def execute(self, args):
        """ client side, returns (bool,*) """
        logging.debug("    CS Execute")
        ret = eval(args)
        return True, ret


