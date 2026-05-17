dofile('bots/Buff/Helper')

if GPM == nil
then
    GPM = {}
end

function GPM.UpdateGold(bot, gold)
    local gameTime = Helper.DotaTime()

	if gameTime < 0 then return end
	if gameTime > 1200 then gold = gold * 2 end
	if not bot:IsAlive() then gold = gold * 3 end

	bot:ModifyGold(gold, true, 0)
end

return GPM
