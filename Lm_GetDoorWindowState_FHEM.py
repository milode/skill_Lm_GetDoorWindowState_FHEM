from core.base.model.AliceSkill import AliceSkill
from core.dialog.model.DialogSession import DialogSession
from core.util.Decorators import IntentHandler


class Lm_GetDoorWindowState_FHEM(AliceSkill):
	"""
	Author: milode
	Description: Liefert den tür und fenster status von fhem
	"""

	@IntentHandler('GetDoorWindowState')
	def dummyIntent1(self, session: DialogSession, **_kwargs):
		pass
