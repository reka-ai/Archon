from archon import Archon
from reka.client import Reka

# make sure to set your OPENAI_API_KEY environment variable

# Initialize Archon
single_gpt_config = {
    "name": "gpt-4o-single",
    "layers": [
        [
            {
                "type": "generator",
                "model": "gpt-4o",
                "model_type": "OpenAI_API",
                "top_k": 1,
                "temperature": 0.7,
                "max_tokens": 2048,
                "samples": 1,
            }
        ]
    ],
}


multi_gpt_config = {
    "name": "reka-multi-model",
    "layers": [
        [
            {
                "type": "generator",
                "model": "reka-flash",
                "model_type": "Reka_API",
                "top_k": 1,
                "temperature": 0.4,
                "max_tokens": 2048,
                "samples": 10,
                "no_system": True,
            }
        ],
        [
            {
                "type": "ranker",
                "model": "reka-flash",
                "model_type": "Reka_API",
                "top_k": 5,
                "temperature": 0.4,
                "max_tokens": 2048,
                "no_system": True,
            }
        ],
        [
            {
                "type": "fuser",
                "model": "reka-flash",
                "model_type": "Reka_API",
                "temperature": 0.4,
                "max_tokens": 2048,
                "samples": 1,
                "no_system": True,
            }
        ],
    ],
}

reka_config = {
    "name": "reka-flash",
    "layers": [
        [
            {
                "type": "generator",
                "model": "reka-flash",  # will be passed to generator as an arg
                "model_type": "Reka_API",
                "temperature": 0.4,
                "max_tokens": 2048,
                "samples": 1,
                "no_system": True,
            }
        ],
    ],
}

#################################################

single_gpt = Archon(reka_config)
multi_gpt = Archon(multi_gpt_config)

testing_instruction = [{"role": "user", "content": "How do I make a cake?"}]

single_gpt_response = single_gpt.generate(testing_instruction)
#multi_gpt_response = multi_gpt.generate(testing_instruction)

print(f"Single GPT Query: {single_gpt_response}")
# print("---------------------")
# print(f"Multi GPT Query: {multi_gpt_response}")
