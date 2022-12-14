from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
# bu til uchun
til = ReplyKeyboardMarkup(
	keyboard = [
	[
		KeyboardButton(text = "ðºð¿ O'zbekcha"),
		KeyboardButton(text = 'ð·ðº Russkiy'),
		KeyboardButton(text = 'ð¬ð§ English')
		],
	],
	resize_keyboard = True
)
# Bu pastki menu uchun
javob = ReplyKeyboardMarkup(
	keyboard = [
	[
		KeyboardButton(text = 'ð¥ Buyurtma berish:')
	],
	[
		
		KeyboardButton(text = 'âï¸ Sozlamalar'),
		KeyboardButton(text = 'ð Biz bilan bog\'lanish')

		],
	],
	resize_keyboard = True
)
# inline menu uchun
inline_javob = InlineKeyboardMarkup(
	inline_keyboard = [
	[
		InlineKeyboardButton(text = 'ð« Lavash ð«',callback_data='lavash'),
		InlineKeyboardButton(text = 'ð­ Hot-Dog ð­',callback_data='hot-dog')
	],
	[
		InlineKeyboardButton(text = 'ð¥ª Sendwich-club ð¥ª',callback_data='sendwich-club'),
		InlineKeyboardButton(text = 'ð® Shaurma ð®',callback_data='shaurma')
	],
	[
		InlineKeyboardButton(text = 'ð Burger ð',callback_data='burger'),
		InlineKeyboardButton(text = 'ð¥ Donar ð¥',callback_data='donar')
	],
	[
		
		InlineKeyboardButton(text = 'ð Gazaklar ð',callback_data='gazaklar'),
		InlineKeyboardButton(text = 'ð¥¤âï¸ Ichimliklar ð¥¤âï¸',callback_data='ichimliklar')
	],
	[
		
		InlineKeyboardButton(text = 'ð° Desertlar ð°',callback_data='desert'),
		InlineKeyboardButton(text = 'ðPizza ð',callback_data='pizza')
	],
	],	
)

# lavashni bosganda menyu
#=========================================================================================================
#=========================================================================================================
#=========================================================================================================
lavash_menu = InlineKeyboardMarkup(
	inline_keyboard = [
	[
		InlineKeyboardButton(text = 'ð¥© Mol go\'shti ð¥©',callback_data='mol-goshtlik'),
		InlineKeyboardButton(text = 'ð¥©ð¶ Qalampirli mol go\'shti ð¥©ð¶',callback_data='qmolgoshtlik')
	],
	[
		
		InlineKeyboardButton(text = 'ð Tovuq go\'shti ð',callback_data='tovuqli'),
		InlineKeyboardButton(text = 'ðð¶ Qalampirli Tovuq go\'shti ðð¶',callback_data='qtovuqli')

	],
	[
		InlineKeyboardButton(text = 'ð¥¬ð¥ Fitter ð¥¬ð¥',callback_data = 'fitter')
	],
	[
		InlineKeyboardButton(text = 'â©ï¸ Ortga',callback_data = 'ortga')
	],
	],
	
)
#lavash_mol_gushtlik_menu uchun
#=========================================================================================================
lavash_mol_gushtlik_menu = InlineKeyboardMarkup(
	inline_keyboard = [
	[
		InlineKeyboardButton(text = 'ð¤ð¤ Mini ð¤ð¤',callback_data='mini'),
		InlineKeyboardButton(text = 'ð¤ð¤ Klassik ð¤ð¤',callback_data='klassik')
	],
	[
		InlineKeyboardButton(text = 'â©ï¸ Ortga',callback_data='ortga_2'),
	],
	]
	
)
# mini uchun raqamlar
lavash_mol_gushtli_mini = InlineKeyboardMarkup(
	inline_keyboard = [
	[
		InlineKeyboardButton(text = '1ï¸â£',callback_data='1'),
		InlineKeyboardButton(text = '2ï¸â£',callback_data='2'),
		InlineKeyboardButton(text = '3ï¸â£',callback_data='3')
	],
	[
		InlineKeyboardButton(text = '4ï¸â£',callback_data='4'),
		InlineKeyboardButton(text = '5ï¸â£',callback_data='5'),
		InlineKeyboardButton(text = '6ï¸â£',callback_data='6')
	],
	[
		InlineKeyboardButton(text = '7ï¸â£',callback_data='7'),
		InlineKeyboardButton(text = '8ï¸â£',callback_data='8'),
		InlineKeyboardButton(text = '9ï¸â£',callback_data='9')
	],
	[
		InlineKeyboardButton(text = 'â©ï¸ Ortga',callback_data='ortga_3'),
	],
	],
	
)
# klassik uchun raqamlar
lavash_mol_gushtli_klassik = InlineKeyboardMarkup(
	inline_keyboard = [
	[
		InlineKeyboardButton(text = '1ï¸â£',callback_data='1'),
		InlineKeyboardButton(text = '2ï¸â£',callback_data='2'),
		InlineKeyboardButton(text = '3ï¸â£',callback_data='3')
	],
	[
		InlineKeyboardButton(text = '4ï¸â£',callback_data='4'),
		InlineKeyboardButton(text = '5ï¸â£',callback_data='5'),
		InlineKeyboardButton(text = '6ï¸â£',callback_data='6')
	],
	[
		InlineKeyboardButton(text = '7ï¸â£',callback_data='7'),
		InlineKeyboardButton(text = '8ï¸â£',callback_data='8'),
		InlineKeyboardButton(text = '9ï¸â£',callback_data='9')
	],
	[
		InlineKeyboardButton(text = 'â©ï¸ Ortga',callback_data='ortga_4'),
	],
	],
	
)
#=========================================================================================================
#lavash_tovuq_gushtlik_menu uchun
lavash_tovuq_gushtlik_menu = InlineKeyboardMarkup(
	inline_keyboard = [
	[
		InlineKeyboardButton(text = 'ð¤ð¤ Mini ð¤ð¤',callback_data='mini1'),
		InlineKeyboardButton(text = 'ð¤ð¤ Klassik ð¤ð¤',callback_data='klassik1')
	],
	[
		InlineKeyboardButton(text = 'â©ï¸ Ortga',callback_data='ortga_5'),
	],
	]
	
)
# lavash tovuq go'shtlik mini
lavash_tovuq_gushtli_mini = InlineKeyboardMarkup(
	inline_keyboard = [
	[
		InlineKeyboardButton(text = '1ï¸â£',callback_data='1'),
		InlineKeyboardButton(text = '2ï¸â£',callback_data='2'),
		InlineKeyboardButton(text = '3ï¸â£',callback_data='3')
	],
	[
		InlineKeyboardButton(text = '4ï¸â£',callback_data='4'),
		InlineKeyboardButton(text = '5ï¸â£',callback_data='5'),
		InlineKeyboardButton(text = '6ï¸â£',callback_data='6')
	],
	[
		InlineKeyboardButton(text = '7ï¸â£',callback_data='7'),
		InlineKeyboardButton(text = '8ï¸â£',callback_data='8'),
		InlineKeyboardButton(text = '9ï¸â£',callback_data='9')
	],
	[
		InlineKeyboardButton(text = 'â©ï¸ Ortga',callback_data='ortga_6'),
	],
	],
	
)
# lavash tovuq go'shtlik klassik
lavash_tovuq_gushtli_klassik = InlineKeyboardMarkup(
	inline_keyboard = [
	[
		InlineKeyboardButton(text = '1ï¸â£',callback_data='1'),
		InlineKeyboardButton(text = '2ï¸â£',callback_data='2'),
		InlineKeyboardButton(text = '3ï¸â£',callback_data='3')
	],
	[
		InlineKeyboardButton(text = '4ï¸â£',callback_data='4'),
		InlineKeyboardButton(text = '5ï¸â£',callback_data='5'),
		InlineKeyboardButton(text = '6ï¸â£',callback_data='6')
	],
	[
		InlineKeyboardButton(text = '7ï¸â£',callback_data='7'),
		InlineKeyboardButton(text = '8ï¸â£',callback_data='8'),
		InlineKeyboardButton(text = '9ï¸â£',callback_data='9')
	],
	[
		InlineKeyboardButton(text = 'â©ï¸ Ortga',callback_data='ortga_7'),
	],
	],
	
)

#=========================================================================================================
lavash_mol_gushtlik_menu = InlineKeyboardMarkup(
	inline_keyboard = [
	[
		InlineKeyboardButton(text = 'ð¤ð¤ Mini ð¤ð¤',callback_data='mini2'),
		InlineKeyboardButton(text = 'ð¤ð¤ Klassik ð¤ð¤',callback_data='klassik2')
	],
	[
		InlineKeyboardButton(text = 'â©ï¸ Ortga',callback_data='ortga_8'),
	],
	]
	
)

lavash_qalampir_mol_gushtli_mini = InlineKeyboardMarkup(
	inline_keyboard = [
	[
		InlineKeyboardButton(text = '1ï¸â£',callback_data='1'),
		InlineKeyboardButton(text = '2ï¸â£',callback_data='2'),
		InlineKeyboardButton(text = '3ï¸â£',callback_data='3')
	],
	[
		InlineKeyboardButton(text = '4ï¸â£',callback_data='4'),
		InlineKeyboardButton(text = '5ï¸â£',callback_data='5'),
		InlineKeyboardButton(text = '6ï¸â£',callback_data='6')
	],
	[
		InlineKeyboardButton(text = '7ï¸â£',callback_data='7'),
		InlineKeyboardButton(text = '8ï¸â£',callback_data='8'),
		InlineKeyboardButton(text = '9ï¸â£',callback_data='9')
	],
	[
		InlineKeyboardButton(text = 'â©ï¸ Ortga',callback_data='ortga_9'),
	],
	],
	
)
# lavash qalampir mol go'shtlik klassik
lavash_qalampir_mol_gushtli_klassik = InlineKeyboardMarkup(
	inline_keyboard = [
	[
		InlineKeyboardButton(text = '1ï¸â£',callback_data='1'),
		InlineKeyboardButton(text = '2ï¸â£',callback_data='2'),
		InlineKeyboardButton(text = '3ï¸â£',callback_data='3')
	],
	[
		InlineKeyboardButton(text = '4ï¸â£',callback_data='4'),
		InlineKeyboardButton(text = '5ï¸â£',callback_data='5'),
		InlineKeyboardButton(text = '6ï¸â£',callback_data='6')
	],
	[
		InlineKeyboardButton(text = '7ï¸â£',callback_data='7'),
		InlineKeyboardButton(text = '8ï¸â£',callback_data='8'),
		InlineKeyboardButton(text = '9ï¸â£',callback_data='9')
	],
	[
		InlineKeyboardButton(text = 'â©ï¸ Ortga',callback_data='ortga_10'),
	],
	],
	
)

#=========================================================================================================
# Lavash qalampir tovuq go'shtlik menu
lavash_qalampir_tovuq_gushtlik_menu = InlineKeyboardMarkup(
	inline_keyboard = [
	[
		InlineKeyboardButton(text = 'ð¤ð¤ Mini ð¤ð¤',callback_data='mini3'),
		InlineKeyboardButton(text = 'ð¤ð¤ Klassik ð¤ð¤',callback_data='klassik3')
	],
	[
		InlineKeyboardButton(text = 'â©ï¸ Ortga',callback_data='ortga_11'),
	],
	]
	
)
# Lavash qalampir tovuq mini
lavash_qalampir_tovuq_gushtli_mini = InlineKeyboardMarkup(
	inline_keyboard = [
	[
		InlineKeyboardButton(text = '1ï¸â£',callback_data='1'),
		InlineKeyboardButton(text = '2ï¸â£',callback_data='2'),
		InlineKeyboardButton(text = '3ï¸â£',callback_data='3')
	],
	[
		InlineKeyboardButton(text = '4ï¸â£',callback_data='4'),
		InlineKeyboardButton(text = '5ï¸â£',callback_data='5'),
		InlineKeyboardButton(text = '6ï¸â£',callback_data='6')
	],
	[
		InlineKeyboardButton(text = '7ï¸â£',callback_data='7'),
		InlineKeyboardButton(text = '8ï¸â£',callback_data='8'),
		InlineKeyboardButton(text = '9ï¸â£',callback_data='9')
	],
	[
		InlineKeyboardButton(text = 'â©ï¸ Ortga',callback_data='ortga_12'),
	],
	],
	
)
# lavash qalampir mol go'shtlik klassik
lavash_qalampir_tovuq_gushtli_klassik = InlineKeyboardMarkup(
	inline_keyboard = [
	[
		InlineKeyboardButton(text = '1ï¸â£',callback_data='1'),
		InlineKeyboardButton(text = '2ï¸â£',callback_data='2'),
		InlineKeyboardButton(text = '3ï¸â£',callback_data='3')
	],
	[
		InlineKeyboardButton(text = '4ï¸â£',callback_data='4'),
		InlineKeyboardButton(text = '5ï¸â£',callback_data='5'),
		InlineKeyboardButton(text = '6ï¸â£',callback_data='6')
	],
	[
		InlineKeyboardButton(text = '7ï¸â£',callback_data='7'),
		InlineKeyboardButton(text = '8ï¸â£',callback_data='8'),
		InlineKeyboardButton(text = '9ï¸â£',callback_data='9')
	],
	[
		InlineKeyboardButton(text = 'â©ï¸ Ortga',callback_data='ortga_13'),
	],
	],
	
)

fitter = InlineKeyboardMarkup(
	inline_keyboard = [
	[
		InlineKeyboardButton(text = '1ï¸â£',callback_data='1'),
		InlineKeyboardButton(text = '2ï¸â£',callback_data='2'),
		InlineKeyboardButton(text = '3ï¸â£',callback_data='3')
	],
	[
		InlineKeyboardButton(text = '4ï¸â£',callback_data='4'),
		InlineKeyboardButton(text = '5ï¸â£',callback_data='5'),
		InlineKeyboardButton(text = '6ï¸â£',callback_data='6')
	],
	[
		InlineKeyboardButton(text = '7ï¸â£',callback_data='7'),
		InlineKeyboardButton(text = '8ï¸â£',callback_data='8'),
		InlineKeyboardButton(text = '9ï¸â£',callback_data='9')
	],
	[
		InlineKeyboardButton(text = 'â©ï¸ Ortga',callback_data='ortga_19'),
	],
	],
	
)










#=========================================================================================================
#=========================================================================================================
#=========================================================================================================
# Hot-Dog Menu
hot_dog_menu = InlineKeyboardMarkup(
	inline_keyboard = [
	[
		InlineKeyboardButton(text = 'ð­ Hot-dog baget dabl ð­',callback_data='double'),
		InlineKeyboardButton(text = 'ð­ Classic Hot-dog ð­',callback_data='classic')
	],
	[
		
		InlineKeyboardButton(text = 'ð Tovuqli Hot-dog ð',callback_data='tovuqli'),
		InlineKeyboardButton(text = 'ð±ð­ Korolevskiy Hot-dog ð±ð­',callback_data='korolevskiy')

	],
	[
		InlineKeyboardButton(text = 'â©ï¸ Ortga',callback_data = 'ortga')
	],
	],
)
# Hot-Dog Classic
Hot_dog_klassik = InlineKeyboardMarkup(
	inline_keyboard = [
	[
		InlineKeyboardButton(text = '1ï¸â£',callback_data='1'),
		InlineKeyboardButton(text = '2ï¸â£',callback_data='2'),
		InlineKeyboardButton(text = '3ï¸â£',callback_data='3')
	],
	[
		InlineKeyboardButton(text = '4ï¸â£',callback_data='4'),
		InlineKeyboardButton(text = '5ï¸â£',callback_data='5'),
		InlineKeyboardButton(text = '6ï¸â£',callback_data='6')
	],
	[
		InlineKeyboardButton(text = '7ï¸â£',callback_data='7'),
		InlineKeyboardButton(text = '8ï¸â£',callback_data='8'),
		InlineKeyboardButton(text = '9ï¸â£',callback_data='9')
	],
	[
		InlineKeyboardButton(text = 'â©ï¸ Ortga',callback_data='ortga_15'),
	],
	],
	
)
# Hot-Dog Dabl
Hot_dog_dabl = InlineKeyboardMarkup(
	inline_keyboard = [
	[
		InlineKeyboardButton(text = '1ï¸â£',callback_data='1'),
		InlineKeyboardButton(text = '2ï¸â£',callback_data='2'),
		InlineKeyboardButton(text = '3ï¸â£',callback_data='3')
	],
	[
		InlineKeyboardButton(text = '4ï¸â£',callback_data='4'),
		InlineKeyboardButton(text = '5ï¸â£',callback_data='5'),
		InlineKeyboardButton(text = '6ï¸â£',callback_data='6')
	],
	[
		InlineKeyboardButton(text = '7ï¸â£',callback_data='7'),
		InlineKeyboardButton(text = '8ï¸â£',callback_data='8'),
		InlineKeyboardButton(text = '9ï¸â£',callback_data='9')
	],
	[
		InlineKeyboardButton(text = 'â©ï¸ Ortga',callback_data='ortga_16'),
	],
	],
	
)
# Hot-Dog Korolevskiy
Hot_dog_korolevskiy = InlineKeyboardMarkup(
	inline_keyboard = [
	[
		InlineKeyboardButton(text = '1ï¸â£',callback_data='1'),
		InlineKeyboardButton(text = '2ï¸â£',callback_data='2'),
		InlineKeyboardButton(text = '3ï¸â£',callback_data='3')
	],
	[
		InlineKeyboardButton(text = '4ï¸â£',callback_data='4'),
		InlineKeyboardButton(text = '5ï¸â£',callback_data='5'),
		InlineKeyboardButton(text = '6ï¸â£',callback_data='6')
	],
	[
		InlineKeyboardButton(text = '7ï¸â£',callback_data='7'),
		InlineKeyboardButton(text = '8ï¸â£',callback_data='8'),
		InlineKeyboardButton(text = '9ï¸â£',callback_data='9')
	],
	[
		InlineKeyboardButton(text = 'â©ï¸ Ortga',callback_data='ortga_17'),
	],
	],
	
)
# Hot-Dog Tovuqli
Hot_dog_tovuqli = InlineKeyboardMarkup(
	inline_keyboard = [
	[
		InlineKeyboardButton(text = '1ï¸â£',callback_data='1'),
		InlineKeyboardButton(text = '2ï¸â£',callback_data='2'),
		InlineKeyboardButton(text = '3ï¸â£',callback_data='3')
	],
	[
		InlineKeyboardButton(text = '4ï¸â£',callback_data='4'),
		InlineKeyboardButton(text = '5ï¸â£',callback_data='5'),
		InlineKeyboardButton(text = '6ï¸â£',callback_data='6')
	],
	[
		InlineKeyboardButton(text = '7ï¸â£',callback_data='7'),
		InlineKeyboardButton(text = '8ï¸â£',callback_data='8'),
		InlineKeyboardButton(text = '9ï¸â£',callback_data='9')
	],
	[
		InlineKeyboardButton(text = 'â©ï¸ Ortga',callback_data='ortga_18'),
	],
	],
	
)
#=========================================================================================================
#=========================================================================================================
#=========================================================================================================

donar_menu = InlineKeyboardMarkup(
	inline_keyboard = [
	[
		InlineKeyboardButton(text = 'ð Tovuq-go\'shtlik ð',callback_data='tdonar'),
		InlineKeyboardButton(text = 'ð¥© Mol-goshtlik ð¥©',callback_data='mdonar')
	],
	[
		InlineKeyboardButton(text = 'â©ï¸ Ortga',callback_data='ortga_20'),
	],
	]
	
)
# Donar tovuq go'shtli
Donar_tovuqli = InlineKeyboardMarkup(
	inline_keyboard = [
	[
		InlineKeyboardButton(text = '1ï¸â£',callback_data='1'),
		InlineKeyboardButton(text = '2ï¸â£',callback_data='2'),
		InlineKeyboardButton(text = '3ï¸â£',callback_data='3')
	],
	[
		InlineKeyboardButton(text = '4ï¸â£',callback_data='4'),
		InlineKeyboardButton(text = '5ï¸â£',callback_data='5'),
		InlineKeyboardButton(text = '6ï¸â£',callback_data='6')
	],
	[
		InlineKeyboardButton(text = '7ï¸â£',callback_data='7'),
		InlineKeyboardButton(text = '8ï¸â£',callback_data='8'),
		InlineKeyboardButton(text = '9ï¸â£',callback_data='9')
	],
	[
		InlineKeyboardButton(text = 'â©ï¸ Ortga',callback_data='ortga_21'),
	],
	],
	
)
# Donar mol go'shtli
Donar_mol_gushtli = InlineKeyboardMarkup(
	inline_keyboard = [
	[
		InlineKeyboardButton(text = '1ï¸â£',callback_data='1'),
		InlineKeyboardButton(text = '2ï¸â£',callback_data='2'),
		InlineKeyboardButton(text = '3ï¸â£',callback_data='3')
	],
	[
		InlineKeyboardButton(text = '4ï¸â£',callback_data='4'),
		InlineKeyboardButton(text = '5ï¸â£',callback_data='5'),
		InlineKeyboardButton(text = '6ï¸â£',callback_data='6')
	],
	[
		InlineKeyboardButton(text = '7ï¸â£',callback_data='7'),
		InlineKeyboardButton(text = '8ï¸â£',callback_data='8'),
		InlineKeyboardButton(text = '9ï¸â£',callback_data='9')
	],
	[
		InlineKeyboardButton(text = 'â©ï¸ Ortga',callback_data='ortga_22'),
	],
	],
	
)

#=========================================================================================================
#=========================================================================================================
#=========================================================================================================
# Club sendwich uchun menyu
club_sendwich_menu = InlineKeyboardMarkup(
	inline_keyboard = [
	[
		InlineKeyboardButton(text = 'ð Tovuqli Club-Sendwich ð',callback_data='club_t'),
		InlineKeyboardButton(text = 'ð¥© Classic Club-Sendwich ð¥©',callback_data='club_c')
	],
	[
		InlineKeyboardButton(text = 'â©ï¸ Ortga',callback_data='ortga_23'),
	],
	]
	
)
# Club tovuq go'shtli
Club_tovuqli = InlineKeyboardMarkup(
	inline_keyboard = [
	[
		InlineKeyboardButton(text = '1ï¸â£',callback_data='1'),
		InlineKeyboardButton(text = '2ï¸â£',callback_data='2'),
		InlineKeyboardButton(text = '3ï¸â£',callback_data='3')
	],
	[
		InlineKeyboardButton(text = '4ï¸â£',callback_data='4'),
		InlineKeyboardButton(text = '5ï¸â£',callback_data='5'),
		InlineKeyboardButton(text = '6ï¸â£',callback_data='6')
	],
	[
		InlineKeyboardButton(text = '7ï¸â£',callback_data='7'),
		InlineKeyboardButton(text = '8ï¸â£',callback_data='8'),
		InlineKeyboardButton(text = '9ï¸â£',callback_data='9')
	],
	[
		InlineKeyboardButton(text = 'â©ï¸ Ortga',callback_data='ortga_24'),
	],
	],
	
)
# Club mol go'shtli
Club_classic = InlineKeyboardMarkup(
	inline_keyboard = [
	[
		InlineKeyboardButton(text = '1ï¸â£',callback_data='1'),
		InlineKeyboardButton(text = '2ï¸â£',callback_data='2'),
		InlineKeyboardButton(text = '3ï¸â£',callback_data='3')
	],
	[
		InlineKeyboardButton(text = '4ï¸â£',callback_data='4'),
		InlineKeyboardButton(text = '5ï¸â£',callback_data='5'),
		InlineKeyboardButton(text = '6ï¸â£',callback_data='6')
	],
	[
		InlineKeyboardButton(text = '7ï¸â£',callback_data='7'),
		InlineKeyboardButton(text = '8ï¸â£',callback_data='8'),
		InlineKeyboardButton(text = '9ï¸â£',callback_data='9')
	],
	[
		InlineKeyboardButton(text = 'â©ï¸ Ortga',callback_data='ortga_25'),
	],
	],
	
)
#=========================================================================================================
#=========================================================================================================
#=========================================================================================================
# Shaurma bosganda menyu:
shaurma_menu = InlineKeyboardMarkup(
	inline_keyboard = [
	[
		InlineKeyboardButton(text = 'ð¥© Mol go\'shti ð¥©',callback_data='shaurma_mol-goshtlik'),
		InlineKeyboardButton(text = 'ð¥©ð¶ Qalampirli mol go\'shti ð¥©ð¶',callback_data='shaurma_qmolgoshtlik')
	],
	[
		
		InlineKeyboardButton(text = 'ð Tovuq go\'shti ð',callback_data='shaurma_tovuqli'),
		InlineKeyboardButton(text = 'ðð¶ Qalampirli Tovuq go\'shti ðð¶',callback_data='shaurma_qtovuqli')

	],
	[
		InlineKeyboardButton(text = 'â©ï¸ Ortga',callback_data = 'ortga')
	],
	],
	
)
#shaurma_mol_gushtlik_menu uchun
#=========================================================================================================
shaurma_mol_gushtlik_menu = InlineKeyboardMarkup(
	inline_keyboard = [
	[
		InlineKeyboardButton(text = 'ð¤ð¤ Mini ð¤ð¤',callback_data='shaurma_mini'),
		InlineKeyboardButton(text = 'ð¤ð¤ Klassik ð¤ð¤',callback_data='shaurma_klassik')
	],
	[
		InlineKeyboardButton(text = 'â©ï¸ Ortga',callback_data='ortga_26'),
	],
	]
	
)
# mini uchun raqamlar
shaurma_mol_gushtli_mini = InlineKeyboardMarkup(
	inline_keyboard = [
	[
		InlineKeyboardButton(text = '1ï¸â£',callback_data='1'),
		InlineKeyboardButton(text = '2ï¸â£',callback_data='2'),
		InlineKeyboardButton(text = '3ï¸â£',callback_data='3')
	],
	[
		InlineKeyboardButton(text = '4ï¸â£',callback_data='4'),
		InlineKeyboardButton(text = '5ï¸â£',callback_data='5'),
		InlineKeyboardButton(text = '6ï¸â£',callback_data='6')
	],
	[
		InlineKeyboardButton(text = '7ï¸â£',callback_data='7'),
		InlineKeyboardButton(text = '8ï¸â£',callback_data='8'),
		InlineKeyboardButton(text = '9ï¸â£',callback_data='9')
	],
	[
		InlineKeyboardButton(text = 'â©ï¸ Ortga',callback_data='ortga_27'),
	],
	],
	
)
# klassik uchun raqamlar
shaurma_mol_gushtli_klassik = InlineKeyboardMarkup(
	inline_keyboard = [
	[
		InlineKeyboardButton(text = '1ï¸â£',callback_data='1'),
		InlineKeyboardButton(text = '2ï¸â£',callback_data='2'),
		InlineKeyboardButton(text = '3ï¸â£',callback_data='3')
	],
	[
		InlineKeyboardButton(text = '4ï¸â£',callback_data='4'),
		InlineKeyboardButton(text = '5ï¸â£',callback_data='5'),
		InlineKeyboardButton(text = '6ï¸â£',callback_data='6')
	],
	[
		InlineKeyboardButton(text = '7ï¸â£',callback_data='7'),
		InlineKeyboardButton(text = '8ï¸â£',callback_data='8'),
		InlineKeyboardButton(text = '9ï¸â£',callback_data='9')
	],
	[
		InlineKeyboardButton(text = 'â©ï¸ Ortga',callback_data='ortga_28'),
	],
	],
	
)
#=========================================================================================================
#shaurma_tovuq_gushtlik_menu uchun
shaurma_tovuq_gushtlik_menu = InlineKeyboardMarkup(
	inline_keyboard = [
	[
		InlineKeyboardButton(text = 'ð¤ð¤ Mini ð¤ð¤',callback_data='shaurma_mini1'),
		InlineKeyboardButton(text = 'ð¤ð¤ Klassik ð¤ð¤',callback_data='shaurma_klassik1')
	],
	[
		InlineKeyboardButton(text = 'â©ï¸ Ortga',callback_data='ortga_29'),
	],
	]
	
)
# Shaurma tovuq go'shtlik mini
shaurma_tovuq_gushtli_mini = InlineKeyboardMarkup(
	inline_keyboard = [
	[
		InlineKeyboardButton(text = '1ï¸â£',callback_data='1'),
		InlineKeyboardButton(text = '2ï¸â£',callback_data='2'),
		InlineKeyboardButton(text = '3ï¸â£',callback_data='3')
	],
	[
		InlineKeyboardButton(text = '4ï¸â£',callback_data='4'),
		InlineKeyboardButton(text = '5ï¸â£',callback_data='5'),
		InlineKeyboardButton(text = '6ï¸â£',callback_data='6')
	],
	[
		InlineKeyboardButton(text = '7ï¸â£',callback_data='7'),
		InlineKeyboardButton(text = '8ï¸â£',callback_data='8'),
		InlineKeyboardButton(text = '9ï¸â£',callback_data='9')
	],
	[
		InlineKeyboardButton(text = 'â©ï¸ Ortga â©ï¸',callback_data='ortga_30'),
	],
	],
	
)
# Shaurma tovuq go'shtlik klassik
shaurma_tovuq_gushtli_klassik = InlineKeyboardMarkup(
	inline_keyboard = [
	[
		InlineKeyboardButton(text = '1ï¸â£',callback_data='1'),
		InlineKeyboardButton(text = '2ï¸â£',callback_data='2'),
		InlineKeyboardButton(text = '3ï¸â£',callback_data='3')
	],
	[
		InlineKeyboardButton(text = '4ï¸â£',callback_data='4'),
		InlineKeyboardButton(text = '5ï¸â£',callback_data='5'),
		InlineKeyboardButton(text = '6ï¸â£',callback_data='6')
	],
	[
		InlineKeyboardButton(text = '7ï¸â£',callback_data='7'),
		InlineKeyboardButton(text = '8ï¸â£',callback_data='8'),
		InlineKeyboardButton(text = '9ï¸â£',callback_data='9')
	],
	[
		InlineKeyboardButton(text = 'â©ï¸ Ortga',callback_data='ortga_31'),
	],
	],
	
)

#=========================================================================================================
shaurma_qalampir_mol_gushtlik_menu = InlineKeyboardMarkup(
	inline_keyboard = [
	[
		InlineKeyboardButton(text = 'ð¤ð¤ Mini ð¤ð¤',callback_data='shaurma_mini2'),
		InlineKeyboardButton(text = 'ð¤ð¤ Klassik ð¤ð¤',callback_data='shaurma_klassik2')
	],
	[
		InlineKeyboardButton(text = 'â©ï¸ Ortga',callback_data='ortga_33'),
	],
	]
	
)

shaurma_qalampir_mol_gushtli_mini = InlineKeyboardMarkup(
	inline_keyboard = [
	[
		InlineKeyboardButton(text = '1ï¸â£',callback_data='1'),
		InlineKeyboardButton(text = '2ï¸â£',callback_data='2'),
		InlineKeyboardButton(text = '3ï¸â£',callback_data='3')
	],
	[
		InlineKeyboardButton(text = '4ï¸â£',callback_data='4'),
		InlineKeyboardButton(text = '5ï¸â£',callback_data='5'),
		InlineKeyboardButton(text = '6ï¸â£',callback_data='6')
	],
	[
		InlineKeyboardButton(text = '7ï¸â£',callback_data='7'),
		InlineKeyboardButton(text = '8ï¸â£',callback_data='8'),
		InlineKeyboardButton(text = '9ï¸â£',callback_data='9')
	],
	[
		InlineKeyboardButton(text = 'â©ï¸ Ortga',callback_data='ortga_34'),
	],
	],
	
)
# Shaurma qalampir mol go'shtlik klassik
shaurma_qalampir_mol_gushtli_klassik = InlineKeyboardMarkup(
	inline_keyboard = [
	[
		InlineKeyboardButton(text = '1ï¸â£',callback_data='1'),
		InlineKeyboardButton(text = '2ï¸â£',callback_data='2'),
		InlineKeyboardButton(text = '3ï¸â£',callback_data='3')
	],
	[
		InlineKeyboardButton(text = '4ï¸â£',callback_data='4'),
		InlineKeyboardButton(text = '5ï¸â£',callback_data='5'),
		InlineKeyboardButton(text = '6ï¸â£',callback_data='6')
	],
	[
		InlineKeyboardButton(text = '7ï¸â£',callback_data='7'),
		InlineKeyboardButton(text = '8ï¸â£',callback_data='8'),
		InlineKeyboardButton(text = '9ï¸â£',callback_data='9')
	],
	[
		InlineKeyboardButton(text = 'â©ï¸ Ortga',callback_data='ortga_35'),
	],
	],
	
)

#=========================================================================================================
# Shaurma_ qalampir tovuq go'shtlik menu
shaurma_qalampir_tovuq_gushtlik_menu = InlineKeyboardMarkup(
	inline_keyboard = [
	[
		InlineKeyboardButton(text = 'ð¤ð¤ Mini ð¤ð¤',callback_data='shaurma_mini3'),
		InlineKeyboardButton(text = 'ð¤ð¤ Klassik ð¤ð¤',callback_data='shaurma_klassik3')
	],
	[
		InlineKeyboardButton(text = 'â©ï¸ Ortga',callback_data='ortga_36'),
	],
	]
	
)
# Shaurma qalampir tovuq mini
shaurma_qalampir_tovuq_gushtli_mini = InlineKeyboardMarkup(
	inline_keyboard = [
	[
		InlineKeyboardButton(text = '1ï¸â£',callback_data='1'),
		InlineKeyboardButton(text = '2ï¸â£',callback_data='2'),
		InlineKeyboardButton(text = '3ï¸â£',callback_data='3')
	],
	[
		InlineKeyboardButton(text = '4ï¸â£',callback_data='4'),
		InlineKeyboardButton(text = '5ï¸â£',callback_data='5'),
		InlineKeyboardButton(text = '6ï¸â£',callback_data='6')
	],
	[
		InlineKeyboardButton(text = '7ï¸â£',callback_data='7'),
		InlineKeyboardButton(text = '8ï¸â£',callback_data='8'),
		InlineKeyboardButton(text = '9ï¸â£',callback_data='9')
	],
	[
		InlineKeyboardButton(text = 'â©ï¸ Ortga',callback_data='ortga_37'),
	],
	],
	
)
# shaurma qalampir mol go'shtlik klassik
shaurma_qalampir_tovuq_gushtli_klassik = InlineKeyboardMarkup(
	inline_keyboard = [
	[
		InlineKeyboardButton(text = '1ï¸â£',callback_data='1'),
		InlineKeyboardButton(text = '2ï¸â£',callback_data='2'),
		InlineKeyboardButton(text = '3ï¸â£',callback_data='3')
	],
	[
		InlineKeyboardButton(text = '4ï¸â£',callback_data='4'),
		InlineKeyboardButton(text = '5ï¸â£',callback_data='5'),
		InlineKeyboardButton(text = '6ï¸â£',callback_data='6')
	],
	[
		InlineKeyboardButton(text = '7ï¸â£',callback_data='7'),
		InlineKeyboardButton(text = '8ï¸â£',callback_data='8'),
		InlineKeyboardButton(text = '9ï¸â£',callback_data='9')
	],
	[
		InlineKeyboardButton(text = 'â©ï¸ Ortga',callback_data='ortga_38'),
	],
	],
	
)

#=========================================================================================================
#=========================================================================================================
#=========================================================================================================

# Burger sendwich uchun menyu
burger_menu = InlineKeyboardMarkup(
	inline_keyboard = [
	[
		InlineKeyboardButton(text = 'ðð§ Gamburger ðð§',callback_data='gamburger'),
		InlineKeyboardButton(text = 'ð§ð Chizburger ð§ð',callback_data='chizburger')
	],
	[
		InlineKeyboardButton(text = 'â©ï¸ Ortga',callback_data='ortga'),
	],
	]
	
)
# Burger tovuq go'shtli
gamburger = InlineKeyboardMarkup(
	inline_keyboard = [
	[
		InlineKeyboardButton(text = '1ï¸â£',callback_data='1'),
		InlineKeyboardButton(text = '2ï¸â£',callback_data='2'),
		InlineKeyboardButton(text = '3ï¸â£',callback_data='3')
	],
	[
		InlineKeyboardButton(text = '4ï¸â£',callback_data='4'),
		InlineKeyboardButton(text = '5ï¸â£',callback_data='5'),
		InlineKeyboardButton(text = '6ï¸â£',callback_data='6')
	],
	[
		InlineKeyboardButton(text = '7ï¸â£',callback_data='7'),
		InlineKeyboardButton(text = '8ï¸â£',callback_data='8'),
		InlineKeyboardButton(text = '9ï¸â£',callback_data='9')
	],
	[
		InlineKeyboardButton(text = 'â©ï¸ Ortga',callback_data='ortga_40'),
	],
	],
	
)
# Burger mol go'shtli
chizburger = InlineKeyboardMarkup(
	inline_keyboard = [
	[
		InlineKeyboardButton(text = '1ï¸â£',callback_data='1'),
		InlineKeyboardButton(text = '2ï¸â£',callback_data='2'),
		InlineKeyboardButton(text = '3ï¸â£',callback_data='3')
	],
	[
		InlineKeyboardButton(text = '4ï¸â£',callback_data='4'),
		InlineKeyboardButton(text = '5ï¸â£',callback_data='5'),
		InlineKeyboardButton(text = '6ï¸â£',callback_data='6')
	],
	[
		InlineKeyboardButton(text = '7ï¸â£',callback_data='7'),
		InlineKeyboardButton(text = '8ï¸â£',callback_data='8'),
		InlineKeyboardButton(text = '9ï¸â£',callback_data='9')
	],
	[
		InlineKeyboardButton(text = 'â©ï¸ Ortga',callback_data='ortga_41'),
	],
	],
	
)
#=========================================================================================================
#=========================================================================================================
#=========================================================================================================

ichimliklar_menu = InlineKeyboardMarkup(
	inline_keyboard = [
	[
		InlineKeyboardButton(text = 'ð® Choy va kofe ð®',callback_data='choy_kofe'),
		InlineKeyboardButton(text = 'ð¥¤ð§ Yaxna ichimliklar ð¥¤ð§',callback_data='y_ichimliklar')
	],
	[
		
		InlineKeyboardButton(text = 'ð¹ Fresh va tabiiy soklar ð¹',callback_data='fresh_soklar')

	],
	[
		InlineKeyboardButton(text = 'â©ï¸ Ortga',callback_data = 'ortga')

	],
	]
)
#=========================================================================================================
# Choy kofe menu:
choy_kofe_menu = InlineKeyboardMarkup(
	inline_keyboard = [
	[
		InlineKeyboardButton(text = 'ð® Choy ð®',callback_data='choy'),
		InlineKeyboardButton(text = 'ð® Kofe ð®',callback_data='kofe')
	],
	[
		InlineKeyboardButton(text = 'â©ï¸ Ortga',callback_data='ortga_42'),
	],
	]
	
)
#=========================================================================================================
kofe_menu = InlineKeyboardMarkup(
	inline_keyboard = [
	[
		InlineKeyboardButton(text = 'ð® Americano',callback_data='americano'),
		InlineKeyboardButton(text = ' ð® Latte ð®',callback_data='latte')
	],
	[
		InlineKeyboardButton(text = 'ð® Cappuccino ð®',callback_data='cappuccino'),
		InlineKeyboardButton(text = 'ð® Kofe 3 v 1 ð®',callback_data='cofe_3_in_1')
	],
	[
		InlineKeyboardButton(text = 'â©ï¸ Ortga',callback_data='ortga_43'),
	],
	]
	
)
#=========================================================================================================
# Americano
americano = InlineKeyboardMarkup(
	inline_keyboard = [
	[
		InlineKeyboardButton(text = '1ï¸â£',callback_data='1'),
		InlineKeyboardButton(text = '2ï¸â£',callback_data='2'),
		InlineKeyboardButton(text = '3ï¸â£',callback_data='3')
	],
	[
		InlineKeyboardButton(text = '4ï¸â£',callback_data='4'),
		InlineKeyboardButton(text = '5ï¸â£',callback_data='5'),
		InlineKeyboardButton(text = '6ï¸â£',callback_data='6')
	],
	[
		InlineKeyboardButton(text = '7ï¸â£',callback_data='7'),
		InlineKeyboardButton(text = '8ï¸â£',callback_data='8'),
		InlineKeyboardButton(text = '9ï¸â£',callback_data='9')
	],
	[
		InlineKeyboardButton(text = 'â©ï¸ Ortga',callback_data='ortga_44'),
	],
	],
	
)
#=========================================================================================================
# Latte
latte = InlineKeyboardMarkup(
	inline_keyboard = [
	[
		InlineKeyboardButton(text = '1ï¸â£',callback_data='1'),
		InlineKeyboardButton(text = '2ï¸â£',callback_data='2'),
		InlineKeyboardButton(text = '3ï¸â£',callback_data='3')
	],
	[
		InlineKeyboardButton(text = '4ï¸â£',callback_data='4'),
		InlineKeyboardButton(text = '5ï¸â£',callback_data='5'),
		InlineKeyboardButton(text = '6ï¸â£',callback_data='6')
	],
	[
		InlineKeyboardButton(text = '7ï¸â£',callback_data='7'),
		InlineKeyboardButton(text = '8ï¸â£',callback_data='8'),
		InlineKeyboardButton(text = '9ï¸â£',callback_data='9')
	],
	[
		InlineKeyboardButton(text = 'â©ï¸ Ortga',callback_data='ortga_45'),
	],
	],
	
)
#=========================================================================================================
# Cofe 3 v 1 
cofe_3_in_1 = InlineKeyboardMarkup(
	inline_keyboard = [
	[
		InlineKeyboardButton(text = '1ï¸â£',callback_data='1'),
		InlineKeyboardButton(text = '2ï¸â£',callback_data='2'),
		InlineKeyboardButton(text = '3ï¸â£',callback_data='3')
	],
	[
		InlineKeyboardButton(text = '4ï¸â£',callback_data='4'),
		InlineKeyboardButton(text = '5ï¸â£',callback_data='5'),
		InlineKeyboardButton(text = '6ï¸â£',callback_data='6')
	],
	[
		InlineKeyboardButton(text = '7ï¸â£',callback_data='7'),
		InlineKeyboardButton(text = '8ï¸â£',callback_data='8'),
		InlineKeyboardButton(text = '9ï¸â£',callback_data='9')
	],
	[
		InlineKeyboardButton(text = 'â©ï¸ Ortga',callback_data='ortga_46'),
	],
	],
	
)
#=========================================================================================================
# Cappuccino 
cappuccino = InlineKeyboardMarkup(
	inline_keyboard = [
	[
		InlineKeyboardButton(text = '1ï¸â£',callback_data='1'),
		InlineKeyboardButton(text = '2ï¸â£',callback_data='2'),
		InlineKeyboardButton(text = '3ï¸â£',callback_data='3')
	],
	[
		InlineKeyboardButton(text = '4ï¸â£',callback_data='4'),
		InlineKeyboardButton(text = '5ï¸â£',callback_data='5'),
		InlineKeyboardButton(text = '6ï¸â£',callback_data='6')
	],
	[
		InlineKeyboardButton(text = '7ï¸â£',callback_data='7'),
		InlineKeyboardButton(text = '8ï¸â£',callback_data='8'),
		InlineKeyboardButton(text = '9ï¸â£',callback_data='9')
	],
	[
		InlineKeyboardButton(text = 'â©ï¸ Ortga',callback_data='ortga_47'),
	],
	],
	
)
#=========================================================================================================
choy_menu = InlineKeyboardMarkup(
	inline_keyboard = [
	[
		InlineKeyboardButton(text = "ð Ko'k choy ð",callback_data='kuk'),
		InlineKeyboardButton(text = 'ð Qora choy ð',callback_data='qora')
	],
	[
		InlineKeyboardButton(text = 'ð Limon choy ð',callback_data='limon'),
	],
	[
		InlineKeyboardButton(text = 'â©ï¸ Ortga',callback_data='ortga_48'),
	],
	]
	
)
#=========================================================================================================
qora_choy = InlineKeyboardMarkup(
	inline_keyboard = [
	[
		InlineKeyboardButton(text = '1ï¸â£',callback_data='1'),
		InlineKeyboardButton(text = '2ï¸â£',callback_data='2'),
		InlineKeyboardButton(text = '3ï¸â£',callback_data='3')
	],
	[
		InlineKeyboardButton(text = '4ï¸â£',callback_data='4'),
		InlineKeyboardButton(text = '5ï¸â£',callback_data='5'),
		InlineKeyboardButton(text = '6ï¸â£',callback_data='6')
	],
	[
		InlineKeyboardButton(text = '7ï¸â£',callback_data='7'),
		InlineKeyboardButton(text = '8ï¸â£',callback_data='8'),
		InlineKeyboardButton(text = '9ï¸â£',callback_data='9')
	],
	[
		InlineKeyboardButton(text = 'â©ï¸ Ortga',callback_data='ortga_49'),
	],
	],
	
)
#=========================================================================================================
kuk_choy = InlineKeyboardMarkup(
	inline_keyboard = [
	[
		InlineKeyboardButton(text = '1ï¸â£',callback_data='1'),
		InlineKeyboardButton(text = '2ï¸â£',callback_data='2'),
		InlineKeyboardButton(text = '3ï¸â£',callback_data='3')
	],
	[
		InlineKeyboardButton(text = '4ï¸â£',callback_data='4'),
		InlineKeyboardButton(text = '5ï¸â£',callback_data='5'),
		InlineKeyboardButton(text = '6ï¸â£',callback_data='6')
	],
	[
		InlineKeyboardButton(text = '7ï¸â£',callback_data='7'),
		InlineKeyboardButton(text = '8ï¸â£',callback_data='8'),
		InlineKeyboardButton(text = '9ï¸â£',callback_data='9')
	],
	[
		InlineKeyboardButton(text = 'â©ï¸ Ortga',callback_data='ortga_50'),
	],
	],
	
)
#=========================================================================================================
limon_choy = InlineKeyboardMarkup(
	inline_keyboard = [
	[
		InlineKeyboardButton(text = '1ï¸â£',callback_data='1'),
		InlineKeyboardButton(text = '2ï¸â£',callback_data='2'),
		InlineKeyboardButton(text = '3ï¸â£',callback_data='3')
	],
	[
		InlineKeyboardButton(text = '4ï¸â£',callback_data='4'),
		InlineKeyboardButton(text = '5ï¸â£',callback_data='5'),
		InlineKeyboardButton(text = '6ï¸â£',callback_data='6')
	],
	[
		InlineKeyboardButton(text = '7ï¸â£',callback_data='7'),
		InlineKeyboardButton(text = '8ï¸â£',callback_data='8'),
		InlineKeyboardButton(text = '9ï¸â£',callback_data='9')
	],
	[
		InlineKeyboardButton(text = 'â©ï¸ Ortga',callback_data='ortga_51'),
	],
	],
	
)

#=========================================================================================================
#=========================================================================================================
# Yaxna ichimliklar menyusi:
yaxna_ichimliklar_menu = InlineKeyboardMarkup(
	inline_keyboard = [
	[
		InlineKeyboardButton(text = 'ð¥¤ð§ Coca-cola ð¥¤ð§',callback_data='cola'),
		InlineKeyboardButton(text = 'ð¥¤ð§ Fanta ð¥¤ð§',callback_data='fanta')
	],
	[
		InlineKeyboardButton(text = 'ð¥¤ð§ Sprite ð¥¤ð§',callback_data='sprite'),
		InlineKeyboardButton(text = 'ð¥¤ð§ Nestle ð¥¤ð§',callback_data='nestle')
	],
	[
		InlineKeyboardButton(text = 'â©ï¸ Ortga',callback_data='ortga_52'),
	],
	]
	
)
#=========================================================================================================
cola = InlineKeyboardMarkup(
	inline_keyboard = [
	[
		InlineKeyboardButton(text = '1ï¸â£',callback_data='1'),
		InlineKeyboardButton(text = '2ï¸â£',callback_data='2'),
		InlineKeyboardButton(text = '3ï¸â£',callback_data='3')
	],
	[
		InlineKeyboardButton(text = '4ï¸â£',callback_data='4'),
		InlineKeyboardButton(text = '5ï¸â£',callback_data='5'),
		InlineKeyboardButton(text = '6ï¸â£',callback_data='6')
	],
	[
		InlineKeyboardButton(text = '7ï¸â£',callback_data='7'),
		InlineKeyboardButton(text = '8ï¸â£',callback_data='8'),
		InlineKeyboardButton(text = '9ï¸â£',callback_data='9')
	],
	[
		InlineKeyboardButton(text = 'â©ï¸ Ortga',callback_data='ortga_53'),
	],
	],
	
)

#=========================================================================================================
fanta = InlineKeyboardMarkup(
	inline_keyboard = [
	[
		InlineKeyboardButton(text = '1ï¸â£',callback_data='1'),
		InlineKeyboardButton(text = '2ï¸â£',callback_data='2'),
		InlineKeyboardButton(text = '3ï¸â£',callback_data='3')
	],
	[
		InlineKeyboardButton(text = '4ï¸â£',callback_data='4'),
		InlineKeyboardButton(text = '5ï¸â£',callback_data='5'),
		InlineKeyboardButton(text = '6ï¸â£',callback_data='6')
	],
	[
		InlineKeyboardButton(text = '7ï¸â£',callback_data='7'),
		InlineKeyboardButton(text = '8ï¸â£',callback_data='8'),
		InlineKeyboardButton(text = '9ï¸â£',callback_data='9')
	],
	[
		InlineKeyboardButton(text = 'â©ï¸ Ortga',callback_data='ortga_54'),
	],
	],
	
)

#=========================================================================================================
nestle = InlineKeyboardMarkup(
	inline_keyboard = [
	[
		InlineKeyboardButton(text = '1ï¸â£',callback_data='1'),
		InlineKeyboardButton(text = '2ï¸â£',callback_data='2'),
		InlineKeyboardButton(text = '3ï¸â£',callback_data='3')
	],
	[
		InlineKeyboardButton(text = '4ï¸â£',callback_data='4'),
		InlineKeyboardButton(text = '5ï¸â£',callback_data='5'),
		InlineKeyboardButton(text = '6ï¸â£',callback_data='6')
	],
	[
		InlineKeyboardButton(text = '7ï¸â£',callback_data='7'),
		InlineKeyboardButton(text = '8ï¸â£',callback_data='8'),
		InlineKeyboardButton(text = '9ï¸â£',callback_data='9')
	],
	[
		InlineKeyboardButton(text = 'â©ï¸ Ortga',callback_data='ortga_55'),
	],
	],
	
)

#=========================================================================================================
sprite = InlineKeyboardMarkup(
	inline_keyboard = [
	[
		InlineKeyboardButton(text = '1ï¸â£',callback_data='1'),
		InlineKeyboardButton(text = '2ï¸â£',callback_data='2'),
		InlineKeyboardButton(text = '3ï¸â£',callback_data='3')
	],
	[
		InlineKeyboardButton(text = '4ï¸â£',callback_data='4'),
		InlineKeyboardButton(text = '5ï¸â£',callback_data='5'),
		InlineKeyboardButton(text = '6ï¸â£',callback_data='6')
	],
	[
		InlineKeyboardButton(text = '7ï¸â£',callback_data='7'),
		InlineKeyboardButton(text = '8ï¸â£',callback_data='8'),
		InlineKeyboardButton(text = '9ï¸â£',callback_data='9')
	],
	[
		InlineKeyboardButton(text = 'â©ï¸ Ortga',callback_data='ortga_56'),
	],
	],
	
)
#=========================================================================================================
#=========================================================================================================
# Bliss sok va freshlar uchun menyu
fresh_soklar_menu = InlineKeyboardMarkup(
	inline_keyboard = [
	[
		InlineKeyboardButton(text = 'ðð Bliss ðð',callback_data='bliss'),
		InlineKeyboardButton(text = 'ðð Fresh ðð',callback_data='fresh')
	],
	[
		InlineKeyboardButton(text = 'â©ï¸ Ortga',callback_data='ortga_57'),
	],
	]
	
)
#=========================================================================================================
# Bliss
bliss = InlineKeyboardMarkup(
	inline_keyboard = [
	[
		InlineKeyboardButton(text = '1ï¸â£',callback_data='1'),
		InlineKeyboardButton(text = '2ï¸â£',callback_data='2'),
		InlineKeyboardButton(text = '3ï¸â£',callback_data='3')
	],
	[
		InlineKeyboardButton(text = '4ï¸â£',callback_data='4'),
		InlineKeyboardButton(text = '5ï¸â£',callback_data='5'),
		InlineKeyboardButton(text = '6ï¸â£',callback_data='6')
	],
	[
		InlineKeyboardButton(text = '7ï¸â£',callback_data='7'),
		InlineKeyboardButton(text = '8ï¸â£',callback_data='8'),
		InlineKeyboardButton(text = '9ï¸â£',callback_data='9')
	],
	[
		InlineKeyboardButton(text = 'â©ï¸ Ortga',callback_data='ortga_55'),
	],
	],
	
)
#=========================================================================================================
# Fresh soklari
fresh = InlineKeyboardMarkup(
	inline_keyboard = [
	[
		InlineKeyboardButton(text = '1ï¸â£',callback_data='1'),
		InlineKeyboardButton(text = '2ï¸â£',callback_data='2'),
		InlineKeyboardButton(text = '3ï¸â£',callback_data='3')
	],
	[
		InlineKeyboardButton(text = '4ï¸â£',callback_data='4'),
		InlineKeyboardButton(text = '5ï¸â£',callback_data='5'),
		InlineKeyboardButton(text = '6ï¸â£',callback_data='6')
	],
	[
		InlineKeyboardButton(text = '7ï¸â£',callback_data='7'),
		InlineKeyboardButton(text = '8ï¸â£',callback_data='8'),
		InlineKeyboardButton(text = '9ï¸â£',callback_data='9')
	],
	[
		InlineKeyboardButton(text = 'â©ï¸ Ortga',callback_data='ortga_55'),
	],
	],
	
)

#=========================================================================================================
#=========================================================================================================
#=========================================================================================================
# Gazaklar
gazaklar_menu = InlineKeyboardMarkup(
	inline_keyboard = [
	[
		InlineKeyboardButton(text = 'ð 15 gram Fri ð',callback_data='fri'),
		InlineKeyboardButton(text = 'ð¥ Kartoshka po Derevenski ð¥',callback_data='k_p_der')
	],
	[
		InlineKeyboardButton(text = 'ð Guruch katta ð',callback_data='guruch_katta'),
		InlineKeyboardButton(text = 'ð Guruch kichik ð',callback_data='guruch_kichik')
	],
	[
		InlineKeyboardButton(text = 'â©ï¸ Ortga',callback_data='ortga_56'),
	],
	]
	
)
#=========================================================================================================
guruch_kichik = InlineKeyboardMarkup(
	inline_keyboard = [
	[
		InlineKeyboardButton(text = '1ï¸â£',callback_data='1'),
		InlineKeyboardButton(text = '2ï¸â£',callback_data='2'),
		InlineKeyboardButton(text = '3ï¸â£',callback_data='3')
	],
	[
		InlineKeyboardButton(text = '4ï¸â£',callback_data='4'),
		InlineKeyboardButton(text = '5ï¸â£',callback_data='5'),
		InlineKeyboardButton(text = '6ï¸â£',callback_data='6')
	],
	[
		InlineKeyboardButton(text = '7ï¸â£',callback_data='7'),
		InlineKeyboardButton(text = '8ï¸â£',callback_data='8'),
		InlineKeyboardButton(text = '9ï¸â£',callback_data='9')
	],
	[
		InlineKeyboardButton(text = 'â©ï¸ Ortga',callback_data='ortga_57'),
	],
	],
	
)
#=========================================================================================================
guruch_katta = InlineKeyboardMarkup(
	inline_keyboard = [
	[
		InlineKeyboardButton(text = '1ï¸â£',callback_data='1'),
		InlineKeyboardButton(text = '2ï¸â£',callback_data='2'),
		InlineKeyboardButton(text = '3ï¸â£',callback_data='3')
	],
	[
		InlineKeyboardButton(text = '4ï¸â£',callback_data='4'),
		InlineKeyboardButton(text = '5ï¸â£',callback_data='5'),
		InlineKeyboardButton(text = '6ï¸â£',callback_data='6')
	],
	[
		InlineKeyboardButton(text = '7ï¸â£',callback_data='7'),
		InlineKeyboardButton(text = '8ï¸â£',callback_data='8'),
		InlineKeyboardButton(text = '9ï¸â£',callback_data='9')
	],
	[
		InlineKeyboardButton(text = 'â©ï¸ Ortga',callback_data='ortga_58'),
	],
	],
	
)
#=========================================================================================================
fri = InlineKeyboardMarkup(
	inline_keyboard = [
	[
		InlineKeyboardButton(text = '1ï¸â£',callback_data='1'),
		InlineKeyboardButton(text = '2ï¸â£',callback_data='2'),
		InlineKeyboardButton(text = '3ï¸â£',callback_data='3')
	],
	[
		InlineKeyboardButton(text = '4ï¸â£',callback_data='4'),
		InlineKeyboardButton(text = '5ï¸â£',callback_data='5'),
		InlineKeyboardButton(text = '6ï¸â£',callback_data='6')
	],
	[
		InlineKeyboardButton(text = '7ï¸â£',callback_data='7'),
		InlineKeyboardButton(text = '8ï¸â£',callback_data='8'),
		InlineKeyboardButton(text = '9ï¸â£',callback_data='9')
	],
	[
		InlineKeyboardButton(text = 'â©ï¸ Ortga',callback_data='ortga_59'),
	],
	],
	
)
#=========================================================================================================
kartoshka = InlineKeyboardMarkup(
	inline_keyboard = [
	[
		InlineKeyboardButton(text = '1ï¸â£',callback_data='1'),
		InlineKeyboardButton(text = '2ï¸â£',callback_data='2'),
		InlineKeyboardButton(text = '3ï¸â£',callback_data='3')
	],
	[
		InlineKeyboardButton(text = '4ï¸â£',callback_data='4'),
		InlineKeyboardButton(text = '5ï¸â£',callback_data='5'),
		InlineKeyboardButton(text = '6ï¸â£',callback_data='6')
	],
	[
		InlineKeyboardButton(text = '7ï¸â£',callback_data='7'),
		InlineKeyboardButton(text = '8ï¸â£',callback_data='8'),
		InlineKeyboardButton(text = '9ï¸â£',callback_data='9')
	],
	[
		InlineKeyboardButton(text = 'â©ï¸ Ortga',callback_data='ortga_60'),
	],
	],
	
)

#=========================================================================================================
#=========================================================================================================
#=========================================================================================================

desertlar_menu = InlineKeyboardMarkup(
	inline_keyboard = [
	[
		InlineKeyboardButton(text = 'ð¯ Asal ð¯',callback_data='asal'),
		InlineKeyboardButton(text = 'ð« Shokolad ð«',callback_data='choko')
	],
	[
		InlineKeyboardButton(text = 'ð Qulupnay ð',callback_data='qulupnay'),
	],
	[
		InlineKeyboardButton(text = 'â©ï¸ Ortga',callback_data='ortga_61'),
	],
	]
	
)
#=========================================================================================================

qulupnay = InlineKeyboardMarkup(
	inline_keyboard = [
	[
		InlineKeyboardButton(text = '1ï¸â£',callback_data='1'),
		InlineKeyboardButton(text = '2ï¸â£',callback_data='2'),
		InlineKeyboardButton(text = '3ï¸â£',callback_data='3')
	],
	[
		InlineKeyboardButton(text = '4ï¸â£',callback_data='4'),
		InlineKeyboardButton(text = '5ï¸â£',callback_data='5'),
		InlineKeyboardButton(text = '6ï¸â£',callback_data='6')
	],
	[
		InlineKeyboardButton(text = '7ï¸â£',callback_data='7'),
		InlineKeyboardButton(text = '8ï¸â£',callback_data='8'),
		InlineKeyboardButton(text = '9ï¸â£',callback_data='9')
	],
	[
		InlineKeyboardButton(text = 'â©ï¸ Ortga',callback_data='ortga_62'),
	],
	],
	
)
#=========================================================================================================

shokolad = InlineKeyboardMarkup(
	inline_keyboard = [
	[
		InlineKeyboardButton(text = '1ï¸â£',callback_data='1'),
		InlineKeyboardButton(text = '2ï¸â£',callback_data='2'),
		InlineKeyboardButton(text = '3ï¸â£',callback_data='3')
	],
	[
		InlineKeyboardButton(text = '4ï¸â£',callback_data='4'),
		InlineKeyboardButton(text = '5ï¸â£',callback_data='5'),
		InlineKeyboardButton(text = '6ï¸â£',callback_data='6')
	],
	[
		InlineKeyboardButton(text = '7ï¸â£',callback_data='7'),
		InlineKeyboardButton(text = '8ï¸â£',callback_data='8'),
		InlineKeyboardButton(text = '9ï¸â£',callback_data='9')
	],
	[
		InlineKeyboardButton(text = 'â©ï¸ Ortga',callback_data='ortga_63'),
	],
	],
	
)

#=========================================================================================================

asal = InlineKeyboardMarkup(
	inline_keyboard = [
	[
		InlineKeyboardButton(text = '1ï¸â£',callback_data='1'),
		InlineKeyboardButton(text = '2ï¸â£',callback_data='2'),
		InlineKeyboardButton(text = '3ï¸â£',callback_data='3')
	],
	[
		InlineKeyboardButton(text = '4ï¸â£',callback_data='4'),
		InlineKeyboardButton(text = '5ï¸â£',callback_data='5'),
		InlineKeyboardButton(text = '6ï¸â£',callback_data='6')
	],
	[
		InlineKeyboardButton(text = '7ï¸â£',callback_data='7'),
		InlineKeyboardButton(text = '8ï¸â£',callback_data='8'),
		InlineKeyboardButton(text = '9ï¸â£',callback_data='9')
	],
	[
		InlineKeyboardButton(text = 'â©ï¸ Ortga',callback_data='ortga_64'),
	],
	],
	
)

#=========================================================================================================
#=========================================================================================================
#=========================================================================================================

pizzalar_menu = InlineKeyboardMarkup(
	inline_keyboard = [
	[
		InlineKeyboardButton(text = 'ðð§ Pepperoni ð§ð',callback_data='pepperoni'),
		InlineKeyboardButton(text = 'ðð  Ananaslik Pizza  ðð',callback_data='ananas')
	],
	[
		InlineKeyboardButton(text = 'ðð Margarita ðð',callback_data='margarita'),
	],
	[
		InlineKeyboardButton(text = 'â©ï¸ Ortga',callback_data='ortga'),
	],
	]
	
)
#=========================================================================================================

pepperoni = InlineKeyboardMarkup(
	inline_keyboard = [
	[
		InlineKeyboardButton(text = '1ï¸â£',callback_data='1'),
		InlineKeyboardButton(text = '2ï¸â£',callback_data='2'),
		InlineKeyboardButton(text = '3ï¸â£',callback_data='3')
	],
	[
		InlineKeyboardButton(text = '4ï¸â£',callback_data='4'),
		InlineKeyboardButton(text = '5ï¸â£',callback_data='5'),
		InlineKeyboardButton(text = '6ï¸â£',callback_data='6')
	],
	[
		InlineKeyboardButton(text = '7ï¸â£',callback_data='7'),
		InlineKeyboardButton(text = '8ï¸â£',callback_data='8'),
		InlineKeyboardButton(text = '9ï¸â£',callback_data='9')
	],
	[
		InlineKeyboardButton(text = 'â©ï¸ Ortga',callback_data='ortga_65'),
	],
	],
	
)
#=========================================================================================================

ananas = InlineKeyboardMarkup(
	inline_keyboard = [
	[
		InlineKeyboardButton(text = '1ï¸â£',callback_data='1'),
		InlineKeyboardButton(text = '2ï¸â£',callback_data='2'),
		InlineKeyboardButton(text = '3ï¸â£',callback_data='3')
	],
	[
		InlineKeyboardButton(text = '4ï¸â£',callback_data='4'),
		InlineKeyboardButton(text = '5ï¸â£',callback_data='5'),
		InlineKeyboardButton(text = '6ï¸â£',callback_data='6')
	],
	[
		InlineKeyboardButton(text = '7ï¸â£',callback_data='7'),
		InlineKeyboardButton(text = '8ï¸â£',callback_data='8'),
		InlineKeyboardButton(text = '9ï¸â£',callback_data='9')
	],
	[
		InlineKeyboardButton(text = 'â©ï¸ Ortga',callback_data='ortga_66'),
	],
	],
	
)

#=========================================================================================================

margarita = InlineKeyboardMarkup(
	inline_keyboard = [
	[
		InlineKeyboardButton(text = '1ï¸â£',callback_data='1'),
		InlineKeyboardButton(text = '2ï¸â£',callback_data='2'),
		InlineKeyboardButton(text = '3ï¸â£',callback_data='3')
	],
	[
		InlineKeyboardButton(text = '4ï¸â£',callback_data='4'),
		InlineKeyboardButton(text = '5ï¸â£',callback_data='5'),
		InlineKeyboardButton(text = '6ï¸â£',callback_data='6')
	],
	[
		InlineKeyboardButton(text = '7ï¸â£',callback_data='7'),
		InlineKeyboardButton(text = '8ï¸â£',callback_data='8'),
		InlineKeyboardButton(text = '9ï¸â£',callback_data='9')
	],
	[
		InlineKeyboardButton(text = 'â©ï¸ Ortga',callback_data='ortga_67'),
	],
	],
	
)