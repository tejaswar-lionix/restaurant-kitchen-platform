import React, {useState} from 'react';
export const InventoryView: React.FC = () => {
  const [filter,setFilter]=useState('high');
  return <div><h2>INVENTORY - Inventory - stock, FIFO, waste, counts</h2><p>stock</p></div>
};
export default InventoryView;
