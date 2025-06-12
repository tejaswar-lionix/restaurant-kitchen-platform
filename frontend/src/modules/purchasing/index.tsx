import React, {useState} from 'react';
export const PurchasingView: React.FC = () => {
  const [filter,setFilter]=useState('high');
  return <div><h2>PURCHASING - Purchasing - auto POs, par levels, EOQ</h2><p>auto POs</p></div>
};
export default PurchasingView;
