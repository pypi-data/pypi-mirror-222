from langchain.llms import GPT4All

def interact_with_llm(llm):
    while True:
        query = input("\nEnter a query: ")
        print("Question received: " + query + "\nPlease wait...")
        if query == "exit":
            print("Exiting...")
            break
        if query.strip() == "":
            continue

        # Obtain an answer
        answer = llm(query)
        
        print("\n\n> Question:")
        print(query)
        print(f"\n> Answer:")
        print(answer)


def load_and_interact(model_path, model_n_ctx=1024, model_n_batch=8):
    llm = GPT4All(model=model_path, n_ctx=model_n_ctx, backend='gptj',
                  n_batch=model_n_batch, verbose=False)
    interact_with_llm(llm)
