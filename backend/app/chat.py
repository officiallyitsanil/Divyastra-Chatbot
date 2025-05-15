from app.models.llm import model, tokenizer

chat_history = []

# System prompt that sets the tone
system_prompt = (
    "You are Divyastra, a wise and helpful AI assistant. "
    "Respond in a friendly, clear, and respectful manner.\n\n"
)

def generate_response(prompt):
    global chat_history

    # Save user message
    chat_history.append(("User", prompt))

    # Build conversation string from last 5 messages
    conversation = ""
    for speaker, text in chat_history[-5:]:
        conversation += f"{speaker}: {text}\n"
    conversation += "Divyastra:"

    # Combine with system prompt
    full_prompt = system_prompt + conversation

    # Tokenize and generate
    input_ids = tokenizer(full_prompt, return_tensors="pt").input_ids
    output_ids = model.generate(
        input_ids,
        max_new_tokens=512,  # Ensure large enough output
        do_sample=True,
        top_p=0.9,
        top_k=50,
        temperature=0.7,
        pad_token_id=tokenizer.eos_token_id  # Prevents padding issues
    )

    # Decode and clean the response
    full_output = tokenizer.decode(output_ids[0], skip_special_tokens=True)

    # Extract only the reply after "Divyastra:"
    if "Divyastra:" in full_output:
        reply = full_output.split("Divyastra:")[-1].strip()
    else:
        reply = full_output.strip()

    # Remove anything after "User:" if it appears mistakenly
    if "User:" in reply:
        reply = reply.split("User:")[0].strip()

    # Save the reply
    chat_history.append(("Divyastra", reply))

    # Optional: save to log file
    with open("chat_log.txt", "a", encoding="utf-8") as f:
        f.write(f"{conversation}Divyastra: {reply}\n\n")

    return reply
