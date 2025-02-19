import ell
from ell import Message, ContentBlock
from PIL import Image
from pydantic import BaseModel, Field

message = Message(role="user", content="Hello world")

# print(message)

message = Message(
    role="user",
    content=[
        ContentBlock(text="What is the capital of the moon?"),
        # ContentBlock(image=Image.open("ell-play/cat.jpeg")),
        ContentBlock(text="Here is a picture of a cat"),
    ],
)

# print(message)

message = Message(
    role="user",
    content=[
        "What is the capital of the moon?",
        "Here is a picture of a cat",
    ],
)

# print(message)


class CustomModel(BaseModel):
    value: int


parsed_content = CustomModel(value=42)
message = Message(role="user", content=["Text", ContentBlock(parsed=parsed_content)])

# print(message.parsed)


message = Message(
    role="user",
    content=[
        "Text",
        ContentBlock(parsed=parsed_content),
        ContentBlock(parsed=parsed_content),
    ],
)

# print(message.parsed)


# @ell.simple(model="gpt-4")
# def hello(name: str):
#     """You are a helpful assistant."""
#     return f"Say hello to {name}!"


# print(hello("world"))

ell.init(store="logs")


class MovieReview(BaseModel):
    title: str = Field(description="The title of the movie")
    rating: int = Field(description="The rating of the movie out of 10")
    summary: str = Field(description="A brief summary of the movie")


@ell.complex(model="gpt-4o-2024-08-06", response_format=MovieReview)
def generate_movie_review(movie: str):
    """You are a movie review generator. Given the name of a movie, you need to return a structured review."""
    return f"Generate a review for the movie {movie}"


# review_message = generate_movie_review("The Matrix")
# print(review_message)
# review = review_message.parsed
# print(f"Movie: {review.title}, Rating: {review.rating}/10")
# print(f"Summary: {review.summary}")
# print(review_message.images)


# @ell.complex(model="gpt-4o-2024-08-06")
# def hello(name: str):
#     """You are a movie review generator. Given the name of a movie, you need to return a structured review."""
#     return f"Say hello to {name}"


# hello_result = hello("world")
# print(hello_result.text)
# print(hello_result.parsed)


# @ell.tool()
# def get_weather(
#     location: str = Field(
#         description="The full name of a city and country, e.g. San Francisco, CA, USA"
#     ),
# ):
#     """Get the current weather for a given location."""
#     # Simulated weather API call
#     return f"The weather in {location} is sunny."


# @ell.complex(model="gpt-4-turbo", tools=[get_weather])
# def travel_planner(destination: str):
#     """Plan a trip based on the destination and current weather."""
#     return [
#         ell.system(
#             "You are a travel planner. Use the weather tool to provide relevant advice."
#         ),
#         ell.user(f"Plan a trip to {destination}"),
#     ]


# result = travel_planner("Paris")
# print(result)
# print("RESULT.text")
# print(result.text)  # Prints travel advice
# print("TOOL_CALLS")
# print(result.tool_calls)
# if result.tool_calls:
#     # This is done so that we can pass the tool calls to the language model
#     tool_results = result.call_tools_and_collect_as_message()
#     print("TOOL_RESULTS.text")
#     print(tool_results.text)  # <tool_call>
#     print("TOOL_RESULTS")
#     print(tool_results)

# @ell.tool()
# def create_claim_draft(
#     claim_details: str,
#     claim_type: str,
#     claim_amount: float,
#     claim_date: str = Field(
#         description="The date of the claim in the format YYYY-MM-DD."
#     ),
# ):
#     """Create a claim draft. Returns the claim id created."""  # Tool description
#     print("Create claim draft", claim_details, claim_type, claim_amount, claim_date)
#     return "claim_id-123234"


# claim = create_claim_draft("Claim details", "Claim type", 1000, "2024-01-01")

# print(claim)


# @ell.tool()
# def get_weather(location: str) -> str:
#     # Implementation to fetch weather
#     return f"The weather in {location} is sunny."


# @ell.complex(model="gpt-4", tools=[get_weather])
# def weather_assistant(message_history):
#     return [
#         ell.system(
#             "You are a weather assistant. Use the get_weather tool when needed."
#         ),
#     ] + message_history


# conversation = [ell.user("What's the weather like in New York?")]
# response: ell.Message = weather_assistant(conversation)
# print(response)
# print(response.text)
# print(response.tool_calls)

# if response.tool_calls:
#     tool_results = response.call_tools_and_collect_as_message()
#     print("Tool results:", tool_results)
#     print("Tool results text:", tool_results.text)
#     print("Tool results content:", tool_results.content)

#     # Continue the conversation with tool results
#     final_response = weather_assistant(conversation + [response, tool_results])
#     print("Final response:", final_response.text)


@ell.tool()
def tool1():
    return "Tool 1 result"


@ell.tool()
def tool2():
    return "Tool 2 result"


@ell.tool()
def tool3():
    return "Tool 3 result"


@ell.complex(model="gpt-4", tools=[tool1, tool2, tool3])
def parallel_assistant(message_history):
    return [
        ell.system("You can use multiple tools in parallel."),
    ] + message_history


response = parallel_assistant([ell.user("Perform tasks A, B, and C simultaneously.")])
print(response)
if response.tool_calls:
    tool_results: ell.Message = response.call_tools_and_collect_as_message(
        parallel=True, max_workers=3
    )
    print("Parallel tool results:", tool_results)
