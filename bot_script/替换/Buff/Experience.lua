dofile('bots/Buff/Helper')

if XP == nil
then
    XP = {}
end

function XP.UpdateXP(bot, xp)
    local gameTime = Helper.DotaTime()
    local pid = -1
    if bot.GetPlayerOwnerID ~= nil then pid = bot:GetPlayerOwnerID() end
    if pid < 0 then return end
    if gameTime > 300 then xp = xp + 100 end
    if gameTime > 600 then xp = xp + 100 end
    if gameTime > 900 then xp = xp + 100 end
    if gameTime > 1200 then xp = xp + 100 end
    if gameTime > 1500 then return end
    bot:AddExperience(xp, 0, false, true, pid)
end

return XP