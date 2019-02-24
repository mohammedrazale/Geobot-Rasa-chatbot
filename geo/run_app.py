from rasa_core.channels import HttpInputChannel
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_slack_connector import SlackInput


nlu_interpreter = RasaNLUInterpreter('./models/nlu/default/geonlu')
agent = Agent.load('./models/dialogue', interpreter = nlu_interpreter)

input_channel = SlackInput('xoxp-480050501396-481621180998-560077593863-de3884e3c853080eb0300583cc945b05', #app verification token
							'xoxb-480050501396-558964609748-D0RkEXuFsVBnMLhMpZTPkJat', # bot verification token
							'Qra2UGEN9CapUGEXjRf3CYrA', # slack verification token
							True)

agent.handle_channel(HttpInputChannel(5004, '/', input_channel))
