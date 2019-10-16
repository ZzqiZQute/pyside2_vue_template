<template>
  <div id="app">{{logAckMsg}}</div>
</template>

<script>
import getInterface from "./channel";
export default {
  name: "app",
  components: {},
  data() {
    return {
      logAckMsg: ''
    };
  },
  mounted() {
    getInterface.then(channelInterface => {
      this.interface = channelInterface;
      this.interface.logAck.connect(str => {
        this.logAckMsg = str;
      });
      this.interface.log("Hello world");
    });
  }
};
</script>

<style>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
