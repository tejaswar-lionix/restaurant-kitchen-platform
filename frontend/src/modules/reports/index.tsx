import React, {useState} from 'react';
export const ReportsView: React.FC = () => {
  const [filter,setFilter]=useState('high');
  return <div><h2>REPORTS - Reports - P&L, waste, COGS, variance</h2><p>P&L</p></div>
};
export default ReportsView;
