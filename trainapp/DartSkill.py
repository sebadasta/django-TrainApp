from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.handler_input import HandlerInput
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.utils import is_request_type, is_intent_name
from ask_sdk_model import Response

sb = SkillBuilder()

class LaunchRequestHandler(AbstractRequestHandler):
    """Handler for skill launch."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speech = "Funciona papa!"
        handler_input.response_builder.speak(speech)
        return handler_input.response_builder.response

# Other skill components here ....

class TrainInfoIntentHandler(AbstractRequestHandler):
    """Handler for TrainInfoIntent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name("TrainInfoIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speech = "TrainInfoIntent funciona"
        handler_input.response_builder.speak(speech)
        return handler_input.response_builder.response


      
# Register all handlers, interceptors etc.
# For eg : sb.add_request_handler(LaunchRequestHandler())


sb.add_request_handler(LaunchRequestHandler())
sb.add_request_handler(TrainInfoIntentHandler())


skill = sb.create()