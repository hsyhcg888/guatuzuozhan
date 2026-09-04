export const POSITION_LABELS = { general_manager: '\u603b\u7ecf\u7406', deputy_general_manager: '\u526f\u603b\u7ecf\u7406', section_chief: '\u79d1\u957f', deputy_section_chief: '\u526f\u79d1\u957f', team_leader: '\u7ec4\u957f', member: '\u7ec4\u5458' }
export const ACCOUNT_STATUS_LABELS = { enabled: '\u6b63\u5e38', disabled: '\u5df2\u7981\u7528' }
export const REGISTER_STATUS_LABELS = { pending: '\u5f85\u5ba1\u6838', approved: '\u5df2\u901a\u8fc7', rejected: '\u5df2\u9a73\u56de' }
export const getPositionLabel = (value) => POSITION_LABELS[value] || value || '\u672a\u8bbe\u7f6e'
export const getAccountStatusLabel = (value) => ACCOUNT_STATUS_LABELS[value] || value || '\u672a\u8bbe\u7f6e'
export const getRegisterStatusLabel = (value) => REGISTER_STATUS_LABELS[value] || value || '\u672a\u8bbe\u7f6e'
