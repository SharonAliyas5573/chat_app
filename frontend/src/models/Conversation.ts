import { MessageModel } from './Message';
import { UserModel } from './user';

export interface ConversationModel {
  id: string;
  name: string;
  last_message: MessageModel | null;
  other_user: UserModel;
}