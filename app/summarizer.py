from transformers import pipeline

# 🔁 Replace this with your real local model path
local_model_path = "C:/Users/asult/Models/mT5_multilingual_XLSum"

# Create the summarization pipeline
summarizer = pipeline(
    "summarization",
    model=local_model_path,
    tokenizer=local_model_path
)

def summarize_text(text: str) -> str:
    """
    Arabic text summarization using mT5 multilingual summarizer.
    """
    if not text or text.strip() == "":
        return "❌ لا يمكن تلخيص نص فارغ."

    print(f"\n📥 نص الإدخال:\n{text}\n")

    try:
        result = summarizer(
            text,
            max_new_tokens=100,
            min_length=20,
            do_sample=False,
            repetition_penalty=1.2,
            clean_up_tokenization_spaces=True
        )
        print(f"📤 التلخيص الناتج:\n{result}\n")
        return result[0]['summary_text']
    except Exception as e:
        return f"❌ حدث خطأ أثناء التلخيص: {str(e)}"
