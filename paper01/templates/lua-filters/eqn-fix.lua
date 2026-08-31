-- Fix display math: replace \tag{N} with \qquad(N)
-- because \[...\] doesn't support \tag
-- Also promote inline math with \tag to display math

function Math(el)
  if el.text:match('\\tag%s*%b{}') then
    el.text = el.text:gsub('\\tag%s*(%b{})', function(m)
      local n = m:sub(2, -2)
      return '\\qquad(' .. n .. ')'
    end)
    if el.mathtype == 'InlineMath' then
      el.mathtype = 'DisplayMath'
    end
  end
  return el
end
