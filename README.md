# THM-Sim4IA-25

* Create a file named `OpenAI_token.txt` and put OpenAI key in file
* Create a file named `Gemini_token.txt` and put Gemini key in file
* Download a file:
  `curl -L -o index_CORE.zip "https://th-koeln.sciebo.de/s/8m0j6KWAd48C8Wy/download"`
* Unzip the downloaded index `example_data/index_CORE.zip` file into the `example_data/index_CORE` directory using the following command:
  `unzip index_CORE.zip -d ./example_data/`
* Delete the zip:
  `rm index_CORE.zip`
* Set your `name` and `width_window` in `task_a_1.ipynb`, `task_a_2.ipynb` and `task_b.ipynb`, modify the path to the `./example_data/index_CORE` folder if required
* Run `task_a_1.ipynb` until you've handled all 35 queries
* Run `task_a_2.ipynb` until you've handled all 35 sessions
* Run `task_b.ipynb` until you've handled all 35 sessions
* If you made an error, you can fix it by opening the respective file: `task_A_1--NAME.json`, `task_A_2--NAME.json` or `task_B--NAME.json`