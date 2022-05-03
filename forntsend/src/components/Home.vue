<!--
 * @Descripttion: 
 * @version: 1.0
 * @Author: suanzi
 * @Date: 2022-03-12 08:48:20
 * @LastEditors: suanzi
 * @LastEditTime: 2022-03-25 11:45:15
 * @FilePath: \ZaoZao\forntsend\src\components\Home.vue
-->
<template>
  <div>
    <el-container class="container">
      <el-header>Header</el-header>
      <el-main>Main</el-main>
    </el-container>
  </div>
</template>

<script>
export default {
  name: "Home",
};
</script>

<style>
.el-header {
    background-color: #B3C0D1;
    color: #333;
    text-align: center;
    line-height: 60px;
    height :20%;
  }
  .el-main {
    background-color: #E9EEF3;
    color: #333;
    text-align: center;
    line-height: 160px;
    height :80%;
  }
  .container{
    height: 100%;
    width: 100%;
    background-color: red
  }
</style>