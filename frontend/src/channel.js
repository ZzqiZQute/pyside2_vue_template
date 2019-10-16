import { QWebChannel } from "qwebchannel";

let channelInterface;

export default new Promise(resolve => {
  if (channelInterface) resolve(channelInterface);
  else {
    new QWebChannel(qt.webChannelTransport, channel => {
      channelInterface = channel.objects.channelInterface;
      resolve(channelInterface);
    });
  }
});
