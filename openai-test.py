import pathlib
import textwrap

import google.generativeai as genai

# Used to securely store your API key
#from google.colab import userdata

#from IPython.display import display
#from IPython.display import Markdown


def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

GOOGLE_API_KEY="AIzaSyAYZxBFpb1aBeLO20EKcjPM8Va2KueHaNs"

genai.configure(api_key=GOOGLE_API_KEY)

for m in genai.list_models():
  if 'generateContent' in m.supported_generation_methods:
    print(m.name)

model = genai.GenerativeModel('gemini-pro')
response = model.generate_content(""" Abstract

Introduction: Crohn's disease (CD) is an immune-mediated inflammatory disorder of the gastrointestinal tract with a relapsing-remitting course. Amino acids (AAs) may play critical roles in the intestinal manifestations of disease, due to their involvement in many metabolic and immune functions. The present study aimed to explore serum AA concentrations in adult patients with CD, looking into their variations due to disease activity, surgery and protein content of diet. Eventually, the link between AAs and inflammatory markers was also assessed.

Methods: Consecutive adult patients aged 18-65 years with diagnosis of CD were recruited. All participants underwent anthropometry and were instructed to fill in a 3-day food record to assess protein intake. Disease activity was clinically defined using the Crohn's Disease Activity Index (CDAI), while blood samples were taken to analyze serum AA profile and inflammatory markers.

Results: A total of 103 patients with CD (61 men and 42 women; age:39.9 ± 13.9 years, BMI: 23.4 ± 3.51 kg/m2) were included. Tryptophan levels were found to be remarkably decreased in most subjects, unrelated to disease activity. On the contrary, concentration of lysine, leucine, valine and glutamine decreased in active versus quiescent CD patients, while aspartic acid, glutamate and glycine increased. The latter AAs were also directly correlated with CDAI and serum interleukin (IL)- 1β concentration. Considering the total protein intake, expressed as g/kg/body weight, we observed a reduction in some essential AAs in patients with unmet protein requirements compared to patients who met the recommendation.

Discussion: In conclusion, specific AAs varied according to disease activity and protein intake, adjusted to body weight and disease status. Glu and Asp concentrations raised with increasing IL-1β. However, extensive research is needed to understand the mechanisms underpinning the link between variation in serum AAs, disease activity and protein intake in patients with CD.

According to this abstract can you write me aminoacids that were found associated with Crohn's disease activity and also write if they are increased or decreased' """)
print(response.text)