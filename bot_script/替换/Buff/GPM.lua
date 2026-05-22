dofile('bots/Buff/Helper')

if GPM == nil
then
    GPM = {}
end

function GPM.UpdateGold(bot, gold)
    local gameTime = Helper.DotaTime()
	if gameTime > 300 then gold = gold + 100 end
	if gameTime > 600 then gold = gold + 100 end
	if gameTime > 900 then gold = gold + 100 end
	if gameTime > 1200 then gold = gold + 100 end
	if gameTime > 1500 then return end
	bot:ModifyGold(gold, true, 0)
end

return GPM
