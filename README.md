# From Laptop to Cloud: Self-Hosting Gen AI for Privacy and Performance

|Role|Input/Response|
| --- | --- |
|**User**| help me complete the following sentence: "In the fall of 2022, OpenAI introduced ..."|
|**System**| "In the fall of 2022, OpenAI introduced ChatGPT, a powerful language model that quickly gained popularity for its ability to generate human-like text and assist with a wide range of tasks, from casual conversation to technical problem-solving."|
|**User**| that's you, right?|
|**System**| Yes, that's me! I'm ChatGPT, a language model developed by OpenAI, introduced in the fall of 2022. My purpose is to assist with a wide variety of tasks, including answering questions, providing explanations, generating creative content, and more.|

## The Rise of Generative Artificial Intelligence

### 1950 - 2015

- [What is the history of artificial intelligence (AI)? (Tableau)](https://www.tableau.com/data-insights/ai/history)

  > Birth of AI: 1950-1956: Alan Turing published his work “Computer Machinery and Intelligence” which eventually became The Turing Test, which experts used to measure computer intelligence. The term “artificial intelligence” was coined and came into popular use.

- [A Short History Of ChatGPT: How We Got To Where We Are Today (Forbes, May 19, 2023)](https://www.forbes.com/sites/bernardmarr/2023/05/19/a-short-history-of-chatgpt-how-we-got-to-where-we-are-today/)
  
  > OpenAI was founded in December 2015 by Sam Altman, Greg Brockman, Elon Musk, Ilya Sutskever, Wojciech Zaremba, and John Schulman. The founding team combined their diverse expertise in technology entrepreneurship, machine learning, and software engineering to create an organization focused on advancing artificial intelligence in a way that benefits humanity.


### 2022
- [Introducing ChatGPT, (OpenAI, November 30, 2022)](https://openai.com/index/chatgpt/)

  > We’ve trained a model called ChatGPT which interacts in a conversational way. The dialogue format makes it possible for ChatGPT to answer followup questions, admit its mistakes, challenge incorrect premises, and reject inappropriate requests.
  >
  > ChatGPT is a sibling model to InstructGPT, which is trained to follow an instruction in a prompt and provide a detailed response.
  > 
  > We are excited to introduce ChatGPT to get users’ feedback and learn about its strengths and weaknesses. During the research preview, usage of ChatGPT is free. Try it now at chatgpt.com(opens in a new window).

- [The advent of OpenAI’s ChatGPT may be the most important news event of 2022 (Forbes, December 12, 2022)](https://fortune.com/2022/12/12/openai-chatgpt-biggest-news-event-of-2022/)

  > Russia's invasion of Ukraine tops most lists of important news events in 2022, and President
Volodymyr Zelensky is not only Time's Person of the Year, but also everyone else's. But the last
couple of weeks have convinced me the honor may belong to something else: Open AI's ChatGPT.

- [A new AI chatbot might do your homework for you. But it's still not an A+ student (NPR, December 19, 2022)](https://www.npr.org/2022/12/19/1143912956/chatgpt-ai-chatbot-homework-academia)

  > After the developer OpenAI released the text-based system to the public last month, some educators have been sounding the alarm about the potential that such AI systems have to transform academia, for better and worse.
  >
  > "AI has basically ruined homework," said Ethan Mollick, a professor at the University of Pennsylvania's Wharton School of Business.

### 2023

- [On ChatGPT’s one-year anniversary, it has more than 1.7 billion users—here’s what it may do next (CNBC, November 30, 2023)](https://www.cnbc.com/2023/11/30/chatgpts-one-year-anniversary-how-the-viral-ai-chatbot-has-changed.html)

  > Over the past year, people have used ChatGPT for all sorts of tasks, from writing emails to sprucing up resumes to even creating a six-figure business.
  > 
  > As the ways people utilize the AI chatbot have changed, the technology itself has evolved too.

- [The Year of ChatGPT and Living Generatively (Wired, December 1, 2023)](https://www.wired.com/story/plaintext-chatgpt-year-of-living-generatively/)

  > In November last year, OpenAl launched a "low key research preview" called ChatGPT. What happened next transformed the tech industry-and perhaps humanity's future.

### 2024

- [24 Top AI Statistics And Trends In 2024 (Forbes, Jun 15, 2024)](https://www.forbes.com/advisor/business/ai-statistics/)

  > AI Business Impacts: 43% of businesses are concerned about technology dependence
  > Forty-three percent of businesses are concerned about technology dependence, and an additional **35% worry about having the technical skills to use AI effectively. These concerns highlight the challenges that organizations face while adopting AI technologies.**

## Privacy Concerns for Individuals and Businesses

- [How your data is used to improve model performance (OpenAI)](https://help.openai.com/en/articles/5722486-how-your-data-is-used-to-improve-model-performance)

  > When you use our services for individuals such as ChatGPT or DALL•E, we may use your content to train our models.
  > 
  > We don’t use content from our business offerings such as ChatGPT Team, ChatGPT Enterprise, and our API Platform to train our models. Please see our Enterprise Privacy page for information on how we handle business data. 

- [The tricky truth about how generative AI uses your data (Vox, July 27, 2023)](https://www.vox.com/technology/2023/7/27/23808499/ai-openai-google-meta-data-privacy-nope)

# The Process

1. Tools
2. Research & Experiment
3. Deploy

## 1. Tools

- [An Open-Source Foundation Model](./1-MODELS.md)

  > A publicly available, pre-trained, larege language model that can be hosted on our own compute platform

- [Ollama](https://ollama.com/)

  > An open-source, software framework  that makes it easier to run large language models (LLMs) on a local computer through the use of Modelfiles.

- [Open WebUI](https://docs.openwebui.com/)

  > An extensible, feature-rich, and user-friendly self-hosted WebUI designed to operate entirely offline.

- Compute platform

  > The CPU or GPU enabled systems where models, Ollama, and Open WebUI will run
  
### Researching Models

- [Ollama Model Library](https://ollama.com/library)

  > A collection of open-source FMs that are compatiable with the Ollama hosting environment.

  _Keep in mind the number of parameters used to train the model and how this affects the model's size in GB.  Generally speaking, the more parameters used to train the model, the larger the model will be.  Consider ~5 GB for 8 Billion parameters._

### Model Playgrounds

- [Cloudflare Workers AI LLM Playground](https://playground.ai.cloudflare.com/)

  > Explore different Text Generation models by drafting messages and fine-tuning your responses.
  > Free, no registration

- [Caylent AI Battleground](https://battleground.caylent.com/chat)

  **_I really like this playground but it was generating errors during the last time I tested it (2024-09-04) (MJ)_**

  > Compare models by examining their performance
  > Free, requires registration
  > **_I really like this playground but it was generating errors during the last time I tested it (2024-09-04) (MJ)_**

- Others?

**Experiment with a variety of prompts including:**

- Explain and demonstrate well known algorithms and theorems that can be expressed as code.

  ```
  Explain the Pythagorean theorem and provide a demonstration using Python.
  ```

  ```
  Describe how Shakespeare's most influential plays have been adapted into films.
  ```

- Analyze or process transcripts and other human generated content.

  - Summarize online meeting transcripts
  - Suggest the content for emails, articles, etc. given the context and audience
 
**Note and Experiment with the controls including:**

- System Message

  > Provides a role for the model and controls how the AI system handles the output when it encounters an error or an issue that prevents it from generating a response.

- Maximum Output Length (Tokens)

  > Controls the maximum number of tokens that the AI system can generate in a single response. By limiting the maximum output length, the system can prevent truncation of the output or allow more space for long responses.
  >
  > _Note: If the reponse is truncated, use `continue` as the next prompt and optionally increase Maximum Output Length.  The model should continue responding to the initial prompt._

- Temperature

  > Controls the randomness and/or creativity of the output. Lower temperatures provide less random output.  Higher temperatures provide output that is more random.  The temperature is related to the concept of [Boltzmann temperature in statistical mechanics](https://en.wikipedia.org/wiki/Boltzmann_distribution), where a higher temperature corresponds to more random and exploratory sampling from the probability distribution.

## Ollama and Open Web UI

### Pros and Upsides
### Cons and Downsides

## Installing Ollama and Open Web UI on a Laptop _(With Demonstration)_

### Hardware and Operating System Requirements
- CPU/GPU, RAM, and Disk
- Mac
- Windows
- Linux

## Installing Ollama and Openeb Web UI on a Cloud Server _(With Demonstration)_

### Hardware and Operating System Requirements
- CPU/GPU, RAM, and Disk
- LInux
- AMI Selection
- Costs

## Advanced Hosting in the Cloud _(With Demonstration)_

### Hardware and Operating System Requirements
- CPU/GPU, RAM, and Disk
- LInux
- AMI Selection
- Multiple Servers (For high availability and advanced model support)
- Hosted Zone
- SSL Certificates
- Costs
