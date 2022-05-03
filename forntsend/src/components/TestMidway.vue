<!--
 * @Descripttion: 
 * @version: 1.0
 * @Author: suanzi
 * @Date: 2022-05-02 15:56:52
 * @LastEditors: suanzi
 * @LastEditTime: 2022-05-02 16:27:28
 * @FilePath: \forntsend\src\components\TestMidway.vue
-->
<template>
  <div>
      <button type="button" @click="getUser">点我获取用户</button>
      <div v-if="isHas">
          <ul>
              <li v-for="item in data" :key="item.id">
                  {{item.id}}<br>
                  {{item.name}}<br>
                  {{item.age}}<br>
                  {{item.address}}<br>
                  {{item.phone}}<br>
              </li>
          </ul>
      </div>
  </div>
</template>

<script>
export default {
    name: "TestMidway",
    data (){
        return {
            data:[],
            isHas:false
        }
    },
    methods:{
        getUser(){
            this.$http.get('http://127.0.0.1:7001/api/get_alluser').then((result) => {
                console.log(result);
                this.data=result.data.data;
                console.log(this.data);
                this.isHas=!this.isHas
            }).catch((err) => {
                
            });
        }
    }
}
</script>

<style>

</style>