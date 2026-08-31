-- Claim Extraction Filter for Σ-Model Paper
-- Extracts <!-- CLAIM:C-XXX --> anchors from paper.md
-- and writes them to docs/claims-anchors.log for CI verification

function RawBlock(el)
    if el.text:match("CLAIM:") then
        local file = io.open("docs/claims-anchors.log", "a")
        if file then
            file:write(el.text:match("CLAIM:[%w%-]+") .. "\n")
            file:close()
        end
    end
    return nil
end
