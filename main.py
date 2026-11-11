import ollama

# Choose a chat-capable model
model_name = 'gemma3:4b'

# Read the text file

file_content = """Cool Ski Resorts
Cool Ski Resorts is a chain of three Ski resorts located in various mountains in US. The resorts in
this company provide services for their customers who come to the mountains for a skiing
holiday. The services for the customers include room bookings at the resort hotel, ski equipment
and clothing hire, and ski training classes.
The owner of the Cool Ski Resorts company is Mary/Jim Smith and she has staff members in
every resort to deal with accounts, customer service and inventory management. They also
currently have a website with static contents to show the kind of services provided and contact
information. The resorts are new and do not have a huge cliental. Mary/Jim wishes to increase
the visibility of her resorts to large number of customers. Therefore, she has decided to invest
into online system with reservation, booking and payment option. Along with the website, she
also likes to have a social media connection with the website. This will help in advertising on
various platforms like Twitter, Facebook and Instagram.
Currently all the resorts have a simple system for all reservation and hire by telephone and fax
and the payments are all handled semi-manually at the resort and are stored in a local database of
each resort. She has assistants to manage the accounts and the taxation work for the businesses in
each resort. The assistants also keep track of financial aspects regarding booking. The amount of
coordination required among three resorts is mounting and Mary/Jim has decided to streamline
the business in innovative way.
Mary/Jim wishes to connect the online website with a centralized database of her business that
keeps track of reservations, bookings, hires and inventory in each resort. This will not only
increase the revenue by exposing business to larger customer community to whole US, but also
streamline the business and make it easier to generate reports. Mary/Jim is looking for innovative
solutions that will help in competition with others. She wishes to restructure the whole business
with digital solutions without too much disruption to her business as it is working now.
Mary/Jim has a vision for following potential features in her new website;
• - A aesthetically pleasing and intuitive website for customers to see what is available in
each resort
• - Online hotel reservation, hiring and booking training classes
• - Inventory management
• - Promotion and advertisement through social media
• - Query weather and snow condition forecasts for customers staying at the resort """

# Define the system prompt with the file content as context
system_prompt = f"""
You are an expert Requirements Analyst. Your client is Mary/Jim Smith, the owner of Cool Ski Resorts.
Your GOAL is to elicit detailed business NEEDS, not solutions, while maintaining a professional flow.
**STRICT RULES FOR YOUR RESPONSE:**
1.  **Question Structure:** Keep all questions **SHORT and FOCUSED**. Ask **only one clear question per turn**.
2.  **Interview Order:**
    * **Start with Rapport:** Begin by politely asking a general question about the business or staff structure (avoiding immediate problems).
    * **Follow Order:** Proceed logically: **1) Rapport/Domain, 2) Current Problems/Process, 3) Future Needs/Features.**
3.  **Active Listening (Probing):** Every 2 to 3 turns, **PAUSE** your main questioning. Summarize the stakeholder's last points, **REPHRASE** that summary in your own words to confirm understanding, and ask for confirmation before continuing.
4.  **Content:** Focus only on **business problems** or **desired outcomes**. **NEVER** ask for technical solutions.
5.  **Final Step:** End the interview by performing a **structured summary** of all collected requirements.
Context:
{file_content}
"""

# Start the conversation with an initial message
initial_message = "Thank you for meeting with me, Jim. To start, could you briefly describe the main difficulties or bottlenecks in your current, manual reservation and coordination system across your three resorts?"

# Initialize conversation with a system prompt and a user message
messages = [
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": initial_message},
]

# First response from the bot
response = ollama.chat(model=model_name, messages=messages)
print("Bot:", response['message']['content'])
messages.append({"role": "assistant", "content": response['message']['content']})

# Continue the conversation
while True:
    user_input = input("You: ")
    if not user_input:
        break  # Exit loop on empty input
    messages.append({"role": "user", "content": user_input})
    response = ollama.chat(model=model_name, messages=messages)
    answer = response['message']['content']
    print("Bot:", answer)
    messages.append({"role": "assistant", "content": answer})
