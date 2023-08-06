import logging
import os
import uuid

import coloredlogs
import dotenv
import openai

from deepchecks_llm_client.client import dc_client
from deepchecks_llm_client.data_types import Tag, EnvType, AnnotationType


def run():
    #coloredlogs.install(level='DEBUG')

    dotenv.load_dotenv()

    # openai.api_key = os.environ.get("OPENAI_API_KEY")
    # print([model['id'] for model in openai.Model.list()['data'] if 'gpt-4' in model['id']])

    deepchecks_api_key = os.environ.get("DEEPCHECKS_LLM_API_KEY")
    # auto_collect=True wraps `openai.ChatCompletion` and `openai.Completion` APIs
    # so any OpenAI invocation will fire an event to deepchecks with the relevant data
    dc_client.init(#host='https://demo.llm.deepchecks.com',
                   #host='https://llm.dev.deepchecks.com',
                   host='http://localhost:8000',
                   api_token=deepchecks_api_key,
                   app_name="ShaysApp",
                   version_name="0.0.1-shayA",
                   env_type=EnvType.PROD,
                   auto_collect=True)


    # for i in range(100):
    #     dc_client.log_interaction(user_input="my user input new4" + str(i),
    #                               model_response="my model response new4" + str(i),
    #                               annotation=AnnotationType.GOOD,
    #                               ext_interaction_id="my_ext_system_id_1234" + str(i))
    #
    # raise Exception

    # Adding context to the call, deepchecks will monitor the context together with any OpenAI's request/response
    #dc_client.set_tags({Tag.USER_ID: "A05fdfbb2035e@gmail.com", Tag.USER_INPUT: "How much is 2 plus 2"})

    # Set up your OpenAI API credentials
    openai.api_key = os.environ.get("OPENAI_API_KEY")
    #dc_client.set_tags({Tag.EXT_INTERACTION_ID: "myid123"})
    chat_completion = openai.ChatCompletion.create(#model="gpt-4-32k",
                                                   model="gpt-3.5-turbo",
                                                   temperature=0.7,
                                                   messages=[{"role": "user", "content": "How much is 2 plus 2?"}])

    # # print the chat completion`
    # print(chat_completion.choices[0].message.content)
    #
    #
    # # Annotating based on openai.id
    # dc_client.annotate(chat_completion.openai_id, annotation=AnnotationType.GOOD)
    #
    # ### Next Iteration ###
    # ######################
    #
    # dc_client.app_name("ShaysApp").version_name("0.0.2-shay").env_type(EnvType.EVAL)
    #
    # user_input = "what is the most dominant color of tulips?"
    # # dc_client.set_tags({Tag.USER_ID: "B05fdfbb2035e@gmail.com",
    # #                     Tag.USER_INPUT: user_input})
    # full_input = f"Answering the following question as you were a gardener: {user_input}"
    # response = openai.Completion.create(
    #   model="text-davinci-003",
    #   prompt=full_input,
    #   temperature=0.5,
    #   max_tokens=150,
    #   top_p=1.0,
    #   frequency_penalty=0.0,
    #   presence_penalty=0.0,
    #   stop=["#", ";"]
    # )
    #
    # print(response.choices[0].text)
    #
    # # Annotating based on openai id
    # dc_client.annotate(response.openai_id, annotation=AnnotationType.BAD)
    #
    # ### Let's Log something manually ###
    # ####################################

    # print("before")
    # dc_client.log_interaction(user_input="my user input",
    #                           model_response="my model response",
    #                           annotation=AnnotationType.GOOD,
    #                           ext_interaction_id="my_ext_system_id_1234")


if __name__ == "__main__":
    #asyncio.run(run())
    run()
