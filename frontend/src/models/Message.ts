import { UserModel } from "./user";
 
export interface MessageModel {
  id: string;
  room: string;
  from_user: UserModel;
  to_user: UserModel;
  content: string;
  timestamp: string;
  read: boolean;
}