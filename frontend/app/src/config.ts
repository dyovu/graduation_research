//接続したいPCのIPアドレスに変える
const raw_host = process.env.REACT_APP_API_HOST || 'localhost:8000'

export const host = `http://${raw_host}`
