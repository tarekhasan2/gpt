import os
import openai


API_KEY = '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'

# openai.organization = "org-4wrRVFemttSaxaEfdWVbWhPt"
openai.api_key = API_KEY

# x = openai.Image.create(
#   prompt = 'A house of rural area',
#   n=2,
#   size="1024x1024"
# )
# print(x)
context = "Hotel Espana anti-viral cleaning products"



response =  openai.Completion.create(
  model="text-davinci-003",
  prompt=f"Write questions based on the text below\n\nText: {context}\n\nQuestions:\n1.",
  max_tokens=20,
  temperature=0
)

print(response)













