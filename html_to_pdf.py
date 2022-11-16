import jinja2
import pdfkit

headline = "INT-010722-96009";
summary = """The main similarity between the keto diet, low carb cycling, and the octavia
diet is that they all involve reducing the amount of carbohydrates that a
person eats. The keto diet is a very low carb diet, and low carb cycling
involves alternating between periods of low carb eating and periods of
higher carb eating. The octavia diet is a moderate carb diet that allows for
some carbs, but focuses on eating mostly healthy fats and proteins.
The speaker discusses how diets usually control the quantity of food intake,
whether it is in calories or macronutrients. They state that it is important to
look at the diet across multiple days, rather than just one, in order to get an
accurate assessment. The speaker then goes on to say that diets manipulate
food choices to change the intake of calories and macronutrients, and that
sometimes these changes are done very precisely, while other times they are
done more loosely.
The diets discussed control quantity to varying levels of precision, with some
being more precise than others. The first diet, Octavia, is focused on weight
loss and is 80-90% precise. The second diet, keto, is also focused on weight
loss and is less precise than Octavia. The third diet, low carb cycling, is less
precise than keto and is focused on weight loss.
The conversation is about the Octavia weight loss diet, which gained
popularity in 2018. The diet plan involves eating six small meals throughout
the day, consisting of five fuelings (snacks) from Optavia and one dinner that
the dieter makes themselves with protein and vegetables."""

timestamps = [
	{
		"timestamp": "0:00:04",
		"text": "The Consistency Project: A Look at the Keto Diet, Low Carb Cycling, and Obtainia"
	},
	{
		"timestamp": "0:01:53",
		"text": "The Different Ways That Diets Control Food Intake"
	},
	{
		"timestamp": "0:03:30",
		"text": "The Three Diets We're Reviewing Today: Optavia, Keto, and Low Carb Cycling"
	},
	{
		"timestamp": "0:06:26",
		"text": "The 5 and 1 Diet Plan from Optavia"
	},
	{
		"timestamp": "0:07:56",
		"text": "The Octavia Diet: A Quick Fix Weight Loss Solution"
	},
	{
		"timestamp": "0:12:23",
		"text": "The Pros and Cons of Optavia"
	}
]

transcript = [
	{
		"speaker": "Ana Kasparian",
		"text": "Hello?"
	},
	{
		"speaker": "Beth Childs",
		"text": "Hello? Good afternoon. Afternoon."
	},
	{
		"speaker": "Ana Kasparian",
		"text": "Good afternoon. Is this Matthew Milieno?"
	},
	{
		"speaker": "Beth Childs",
		"text": "Yeah, it's me."
	},
	{
		"speaker": "Ana Kasparian",
		"text": "Well, thank you so much for taking this call. I really appreciate it. Yes, but before we get started, I'll need to read a compliance statement on my end, if that's okay."
	},
	{
		"speaker": "Beth Childs",
		"text": "Yeah, go ahead."
	},
	{
		"speaker": "Ana Kasparian",
		"text": "Okay, so before we get started, I'm going to read a compliance statement that reiterates which you've already confirmed with stream for the record. If you could listen and agree or not agree at the end, that would be great. First, the call will be recorded so."
	},
	{
		"speaker": "Beth Childs",
		"text": "It can be transferred. May I know your name before that you read?"
	},
	{
		"speaker": "Ana Kasparian",
		"text": "Yes, it's Pav. Yes."
	},
	{
		"speaker": "Beth Childs",
		"text": "Okay. Pad."
	},
]

payload = { "headline": headline, "summary": summary, "timestamps": timestamps, "transcript": transcript }

template_loader = jinja2.FileSystemLoader('./')
template_env = jinja2.Environment(loader=template_loader)
template = template_env.get_template('template.html')
output_html = template.render(payload)

# Change the path of wkhtmltopdf on your filesystem accordingly
pdf_config = pdfkit.configuration(wkhtmltopdf='/usr/local/bin/wkhtmltopdf')
pdf_options = {
	"disable-smart-shrinking": '',
	"encoding": "UTF-8"
}

pdfkit.from_string(output_html, 'test.pdf', configuration=pdf_config, options=pdf_options);
