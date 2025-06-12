import React, {useState} from 'react';
export const ApiView: React.FC = () => {
  const [filter,setFilter]=useState('high');
  return <div><h2>API - API - REST for POS, inventory, recipes</h2><p>POST pos</p></div>
};
export default ApiView;
