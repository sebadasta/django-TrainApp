from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.handler_input import HandlerInput
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.utils import is_request_type, is_intent_name
from ask_sdk_model import Response
from ask_sdk_model.slu.entityresolution import StatusCode
from trainapp.functions import *
import random

speechList = ["No se entiende lo que decís",
             "Hablá claro!",
             "Modulá, por favor",
             "Avisáme cuando puedas hablar claro",
             "Ponele voluntad!"]

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

class KilbarrackInfoIntentHandler(AbstractRequestHandler):
    """Handler for KilbarrackInfoIntent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name("KilbarrackInfoIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response

        slots = handler_input.request_envelope.request.intent.slots
        
        try:
          if slots['destino'].resolutions.resolutions_per_authority[0].status.code == StatusCode.ER_SUCCESS_MATCH:
              
              direction = slots['destino'].value
  
              Station_Info = Alexa_getStationInfo(direction)
  
              print(Station_Info)
    
              speech = ("{}".format(Station_Info))
    
          else:
              speech = random.choice(speechList)
               
        except:   
         speech = random.choice(speechList)
          
        handler_input.response_builder.speak(speech)
        return handler_input.response_builder.response



# Register all handlers, interceptors etc.
# For eg : sb.add_request_handler(LaunchRequestHandler())


sb.add_request_handler(LaunchRequestHandler())
sb.add_request_handler(KilbarrackInfoIntentHandler())


skill = sb.create()