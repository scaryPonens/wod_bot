![DALL·E 2024-04-28 20 32 55 - A digital artwork of a muscular woman acting as a CrossFit coach with cyberpunk elements  She appears partly robotic, featuring visible mechanical joi](https://github.com/scaryPonens/wod_bot/assets/165761/ecdf37fd-e25b-489f-8b0e-16362a54c865)

# wod_bot

Snarky CrossFit coach who gives you random WODs scraped from the CrossFit website

---

Ever wish your CrossFit coach could be as on-demand as your favorite streaming service? Meet CrossSnark, the AI-powered CrossFit coach that's here to shake up your fitness routine with a healthy dose of snark. Whether you're at the gym or in your living room, CrossSnark delivers personalized, random workouts straight from the latest on the CrossFit website—no browsing required.

But CrossSnark isn't just about sweating; it’s about smart training. Have questions on how to log your score or scale your workout? CrossSnark’s got the answers, served up with a side of cheeky humor. Plus, get expert advice on the most effective ways to warm up and cool down, ensuring you train safely and effectively.

With CrossSnark, you get more than just a workout buddy; you get a coach who's as committed to your fitness goals as you are, just with a lot more sass. Ready to get fit, laugh, and maybe even roll your eyes? Let CrossSnark guide the way!

---
# Running the bot

You will need to have Ollama installed on your machine. You can install it by downloading and running the 
[Ollama installer](https://ollama.com/download).

Once you have Ollama installed ensure it is running, and pull the llama3 model:

```bash
ollama pull llama3
```

Then you simply need to install the required python dependencies and run the bot.

```bash
pip install -r requirements.txt
streamlit run app.py
```