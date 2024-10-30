import {host} from '../config'


// type process_data
export default function GetRightArm(){
  const getRightArm = async ()=>{
    console.log('右腕データ取得');
    const url = host + '/get_db_data';
    const response = await fetch(url);
  }
  return getRightArm
}