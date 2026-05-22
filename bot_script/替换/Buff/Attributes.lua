dofile('bots/Buff/Helper')

if Attributes == nil then
    Attributes = {}
end

function Attributes.UpdateAttr(bot, attr)
    local gameTime = Helper.DotaTime()
	if gameTime > 300 then attr = attr + 1 end
	if gameTime > 600 then attr = attr + 1 end
	if gameTime > 900 then attr = attr + 1 end
	if gameTime > 1200 then attr = attr + 1 end
	if gameTime > 1500 then return end
    bot:ModifyStrength(attr)
    bot:ModifyAgility(attr)
    bot:ModifyIntellect(attr)
end

return Attributes
