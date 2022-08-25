# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

from inspect import trace
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
# from get_weather import Weather
# from get_food import IFoodie


# class SendFilm(Action):
#     def name(self) -> Text:
#         return "action_send_film"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         dispatcher.utter_unhappy(attachment={
#             "type": "video",
#             "payload": {
#                 "title": "Watch Below Video",
#                 "src": "https://reurl.cc/ZbGMda"
#             }
#         })
#         return []


# class ActionReplyWeather(Action):

#     def name(self) -> Text:
#         return "action_reply_weather"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         city = tracker.get_slot("city")

#         # if(city[0] == "台"):
#         #     city = f"臺{city[1:]}"

#         data = Weather.get_data(city)
#         dispatcher.utter_message(
#             f"{city}的天氣為{data[0]}，降雨機率 {data[1]}%，氣溫{data[2]}℃ ~ {data[4]}℃"
#         )

#         return []
