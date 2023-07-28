"""
At the command line, only need to run once to install the package via pip:
$ pip install google-generativeai
"""

import streamlit as st
from streamlit_chat import message
import google.generativeai as palm
import random
import time

palm.configure(api_key="AIzaSyDeYshE-LEcHkTca2FjXWlxCXbMjIT72Dc")

st.title("Sentiment_Analysis")


# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

defaults = {
  'model': 'models/text-bison-001',
  'temperature': 0.55,
  'candidate_count': 1,
  'top_k': 40,
  'top_p': 0.95,
  'max_output_tokens': 1024,
  'stop_sequences': [],
  'safety_settings': [],
}
if promt := st.chat_input():
            # Add user message to chat history
          st.session_state.messages.append({"role": "user", "content": promt})
          # Display user message in chat message container
          with st.chat_message("user"):
            st.markdown(promt)
if promt:
            prompt = f""" Sentiment Explanation:
            The text expresses overwhelmingly positive sentiments. Words like "wonderful," "amazing," "perfect," and "delicious" indicate a strong positive tone. The overall sentiment of the text is positive with a high confidence score of 0.92.
            
            Feedback:
            The sentiment analysis model have identified the positive sentiments expressed by using words with strong positive connotations. The high confidence score of 0.92 indicates that the model is quite confident in its classification. However, it's important to note that sentiment analysis can be influenced by the context and language used, so occasional misinterpretations may occur. Nevertheless, this result is consistent with the evident positivity of the given text.
            
            
            input: I agree with time magazines assessment.  They are exciting because they bring a lot of freshness to the workplace which helps us to do better. They are also threatening because of their lack of longer commitment and emotional weakness in the workplace.
            They deserve to be recognized as change force, but they don't really justify the hype given.
            The Fresh workforce brings lots of unconventional ideas, work practices, and huge expectations. Their inherent assumption and/or desire that everything needs to be changed should be tamed. Their lack of understanding of the complex problem is worrisome. They are not very good at making tradeoffs. They want everything at the same time which is a disregard for natural evolution.
            output: Sentiment Explanation:
            The text presents a mixed sentiment with both positive and negative aspects. The positive sentiment is evident in phrases like "exciting," "bring a lot of freshness," and "helps us to do better," indicating enthusiasm towards the Fresh workforce's impact. On the other hand, negative sentiments are expressed through phrases like "threatening," "lack of longer commitment," "emotional weakness," "lack of understanding," and "not very good at making tradeoffs," which point to concerns and drawbacks associated with the Fresh workforce.
            
            Feedback:
            The sentiment analysis model has captured the mixed sentiments in the text. It identified the positive aspects related to the Fresh workforce, such as their excitement and ability to bring freshness and improvement to the workplace. Simultaneously, the model also recognized the negative aspects, including concerns about their shorter commitment, emotional weakness, and difficulty with trade-offs.  
            input: Nowadays this is actually not much needed in my opinion. Everything is available with lot of analytics built in, they have access to all information on the internet so, it is not required to give person-to-person, hand-to-hand. 40% old timers are ready to mentor provided the wavelengths match.
            output: 
            Sentiment Explanation:
            The text conveys a neutral sentiment, which means it lacks strong positive or negative emotions. The overall tone appears to be matter-of-fact and informative, without expressing a particular emotional bias. The statements present a balanced view, discussing the availability of information through analytics and the internet, as well as the readiness of some old-timers to mentor under certain conditions.
            
            Feedback:
            The sentiment analysis model has identified the neutral sentiment in the text. The absence of strong emotions or subjective opinions in the text supports the neutral sentiment classification. 
            input: from personal experience – working from home well over 10 years now – one imp thing is trust. Work-life balance works only if employees are trusted. If they are not trusted, they will act untrustworthy way. In millennial generation – we had parental leaves, flexible working hours, 13 day fortnight (you work extra hours every day to get every second Friday as off) and flexibility in holidays. So, work-life balance tends to revolves around the flexibility and revolves around being trusted. 
            output: Sentiment Explanation:
            The text conveys a positive sentiment, which reflects a favorable view towards the importance of trust and work-life balance in the context of remote work. Positive language is evident in phrases like "important thing is trust," "work-life balance works only if employees are trusted," and "work-life balance tends to revolve around flexibility and being trusted."
            
            Feedback:
            The sentiment analysis model has identified the positive sentiment in the text. The expressions used in the text reflect a positive outlook towards the role of trust and flexibility in maintaining a healthy work-life balance in a remote work environment. 
            input: The main challenge is to make them understand the work and what has to be delivered professionally. The understanding process is much faster but it takes more time to set expectations with them. Once they understand they proceed and are committed but the initial process is very challenging. They demand more information for the work required, they do not like to be given part or piecemeal information. They want the complete holistic picture and to their satisfaction. Only then do they start working which gets tedious at times when there are strict deadlines and someone wants to research on tertiary unimportant aspects.  They cannot be enforced, they want complete guidance and information, and then they deliver very well above expectations. -(can you suggest some positive words for the above negative context)"
            output: Certainly! Here are some positive words and phrases that can be used to reframe the negative context:
            
            1. Opportunity (instead of challenge)
            2. Efficient (instead of takes more time)
            3. Inquisitive (instead of demanding)
            4. Engaging (instead of tedious)
            5. Ambitious goals (instead of strict deadlines)
            6. Key aspects (instead of tertiary unimportant aspects)
            7. Self-motivated (instead of cannot be enforced)
            8. Thorough understanding (instead of want complete guidance and information)
            9. Thorough research (instead of research on tertiary unimportant aspects)
            10. Proactive (instead of excessive information-seeking)
            11. Focus on priorities (instead of consequences of focusing too much)
            12. Deliberate decision-making (instead of stuck in analysis paralysis)
            
            By using more positive language, you can shift the perspective and promote a more constructive and optimistic outlook on the situation. This can help create a more productive and harmonious work environment.
            input: hi
            output: how can i help you
            input: who is obama?
            output: sorry i cant help you with that
            input: what is 2+2, and other math questions
            output: sorry i cant help you with that
            input: One of the most challenging projects I worked on was during my internship at Company X. I was assigned to develop a mobile app with a tight deadline. The initial requirements were not clearly defined, and there were constant changes from stakeholders. To address this, I proactively scheduled regular meetings with the team and stakeholders to clarify requirements and expectations. I also broke down the project into smaller tasks and set realistic milestones. By maintaining open communication and adaptability, we were able to deliver the app on time and received positive feedback from the users.
            output: Sentiment: Overall, the sentiment in this statement is positive. The candidate discusses a challenging project but focuses on the proactive steps taken to address the difficulties and achieve success. The use of phrases like "proactively scheduled regular meetings," "clarify requirements and expectations," "broke down the project," "set realistic milestones," and "maintaining open communication and adaptability" reflects a positive attitude towards problem-solving and teamwork. Additionally, the statement concludes with a positive outcome - delivering the app on time and receiving positive feedback from users, which further contributes to the positive sentiment.
            
            Feedback:
            
            Overall, your response to the challenging project during your internship at Company X was well-structured and detailed. You effectively highlighted the obstacles you faced, such as the undefined initial requirements and constant changes from stakeholders. Your proactive approach in scheduling meetings, clarifying requirements, breaking down the project, and setting realistic milestones demonstrated strong problem-solving skills and adaptability.
            
            Additionally, you emphasized the importance of open communication and collaboration, which are crucial qualities in any team environment. The positive outcome of delivering the app on time and receiving positive feedback from users showcases your ability to effectively handle challenges and achieve successful results.
            input: One of the key positive traits that defines me is my relentless determination. When faced with challenges, I don't back down easily. Instead, I see them as opportunities for growth and improvement. For example, at my previous job, we encountered a project that seemed impossible to complete within the given deadline. While some team members became disheartened, I took the lead to motivate everyone and explore alternative solutions. In the end, we successfully completed the project ahead of schedule, and it was a tremendous learning experience for all of us.(what are the negative words used in above given transcript by me?)
            output: The negative words used in the above transcript are "impossible," "disheartened," and "ahead of schedule." The word "impossible" is used to describe the project that the team was working on, which was seen as a challenge. The word "disheartened" is used to describe the team members who became discouraged when they realized that the project was difficult. The word "ahead of schedule" is used to describe the fact that the team was able to complete the project before the deadline, which was a positive outcome.
            input: {promt}
            output:"""

            response = palm.generate_text(
            **defaults,
            prompt=prompt
            )
            
            def response_api():
                return("AI: ",response.result)
            a = response_api()

            # Display assistant response in chat message container
            with st.chat_message("assistant"):
                message_placeholder = st.empty()
                full_response = ""
                assistant_response = a
            # Simulate stream of response with milliseconds delay
                for chunk in assistant_response:
                    full_response += chunk + " "
                    # Add a blinking cursor to simulate typing
                    message_placeholder.markdown(full_response + "▌")
                message_placeholder.markdown(full_response)
            # Add assistant response to chat history
            st.session_state.messages.append({"role": "assistant", "content": full_response})


        
