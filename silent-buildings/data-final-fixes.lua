local function disable_idle_sounds(entity)
    local working_sound = entity.working_sound
    if not working_sound then
        return
    end

    local idle_sound = working_sound.idle_sound
    if not idle_sound then
        return
    end

    idle_sound.volume = 0.0
end

for _, t in pairs({"assembling-machine", "furnace"}) do
    for _, e in pairs(data.raw[t]) do
        disable_idle_sounds(e)
    end
end
