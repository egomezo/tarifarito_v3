<template>
  <div class="components-container" style="border: 0px solid red; margin: 0;">
    <el-row>
      <el-col :span="24">
        <div style="border: 2px solid #C0C4CC; padding: 1%; padding-bottom: 0%; background-color: white; border-radius: 5px;">
          <el-row>
            <el-col :span="2" style="border: 0px solid; color: black;">
              <div style="text-align: center;">
                <img v-if="logo" :src="logo" width="100" height="auto">
              </div>
            </el-col>
            <el-col :span="22" style="border: 0px solid; padding-left: 2%;">
              <el-row>
                <el-col :span="24" style="border: 0px solid red; text-align: center;">
                  <aside>
                    <span style="color: black; font-size: 170%;"><b>DIRECCIÓN TÉCNICA DE GESTIÓN DE ENERGÍA</b></span>
                  </aside>
                </el-col>
                <el-col :span="24" style="border: 0px solid red; text-align: center;">
                  <aside>
                    <span style="font-size: 120%;"><b>{{ name }}</b></span>
                    <!-- <input type="text" v-on:input="(event) => this.$emit('inputChange', event)"> -->
                  </aside>
                </el-col>
              </el-row>
            </el-col>
          </el-row>
        </div>
        <br>
        <div class="containerCards">
          <el-row>
            <el-col :span="24" style="border: 0px solid; color: black; padding-top: 1em; padding-left: 10em; padding-right: 10em;">
              <span v-for="item in components" :key="item.key" :name="item.key">
                <span v-if="item.start === true">
                  <el-card class="box-card" style="border: 2px solid #C0C4CC; padding-left: 2em; padding-right: 2em; margin-bottom: 1em;">
                    <div class="text item">
                      <el-row style="font-weight: bold; padding-bottom: 1%; text-align: center;">
                        <span v-for="cabecera in item.header" :key="cabecera.title">
                          <el-col style="border: 0px solid red; text-align: center;" :span="cabecera.tamano">
                            <span>{{ cabecera.title }}</span>
                          </el-col>
                        </span>
                      </el-row>
                      <el-row style="border: 0px solid blue;">
                        <span v-for="content in item.data" :key="content.campo">
                          <span v-if="content.start === true">
                            <el-col style="border: 0px solid;" class="contentConcept" :span="12">
                              <span class="itemText">{{ content.concepto }}</span>
                            </el-col>
                            <el-col style="border: 0px solid; text-align: center;" class="contentText" :span="4">
                              <span class="itemText">{{ content.unidad }}</span>
                            </el-col>
                            <el-col style="border: 0px solid; text-align: center;" class="contentText" :span="8">
                              <input
                                v-model="values[content.input.key].values"
                                :type="content.input.type"
                                :placeholder="content.input.placeholder"
                                style="width: 75%; height: 2em; margin-bottom: 0.5em;"
                              >
                            </el-col>
                          </span>
                          <span v-else>
                            <span v-if="showCard === content.show">
                              <el-col style="border: 0px solid;" class="contentConcept" :span="12">
                                <span class="itemText">{{ content.concepto }}</span>
                              </el-col>
                              <el-col style="border: 0px solid; text-align: center;" class="contentText" :span="4">
                                <span class="itemText">{{ content.unidad }}</span>
                              </el-col>
                              <el-col style="border: 0px solid; text-align: center;" class="contentText" :span="8">
                                <input
                                  v-model="values[content.input.key].values"
                                  :type="content.input.type"
                                  :placeholder="content.input.placeholder"
                                  style="width: 75%; height: 2em; margin-bottom: 0.5em;"
                                >
                              </el-col>
                            </span>
                          </span>
                        </span>
                      </el-row>
                    </div>
                  </el-card>
                </span>
                <span v-else>
                  <el-card v-if="showCard === item.show" class="box-card" style="border: 2px solid #C0C4CC; padding-left: 2em; padding-right: 2em; margin-bottom: 1em;">
                    <div class="text item">
                      <el-row style="font-weight: bold; padding-bottom: 1%; text-align: center;">
                        <span v-for="cabecera in item.header" :key="cabecera.title">
                          <el-col style="border: 0px solid red; text-align: center;" :span="cabecera.tamano">
                            <span>{{ cabecera.title }}</span>
                          </el-col>
                        </span>
                      </el-row>
                      <el-row style="border: 0px solid blue;">
                        <span v-for="content in item.data" :key="content.campo">
                          <el-col class="contentConcept" :span="12">
                            <span class="itemText">{{ content.concepto }}</span>
                          </el-col>
                          <el-col style="text-align: center;" class="contentText" :span="4">
                            <span class="itemText">{{ content.unidad }}</span>
                          </el-col>
                          <el-col style="text-align: center;" class="contentText" :span="8">
                            <input
                              v-model="values[content.input.key].values"
                              :type="content.input.type"
                              :placeholder="content.input.placeholder"
                              :disabled="true"
                              style="width: 75%; height: 2em; margin-bottom: 0.5em;"
                            >
                          </el-col>
                        </span>
                      </el-row>
                    </div>
                  </el-card>
                </span>
              </span>
            </el-col>
          </el-row>
        </div>
      </el-col>
    </el-row>
    <el-row style="padding-top: 1%;">
      <el-col :span="24" style="text-align: center; border: 0px solid;">
        <el-button type="primary" @click="calcular">Calcular</el-button>
        <el-button v-if="!showCard" type="primary" @click="verificar">Verificado</el-button>
        <el-button v-if="showCard" type="primary" @click="reportar">Reportar</el-button>
      </el-col>
    </el-row>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import logTarifarito from '../../../../../../assets/logo_buho.png'
import componentesTransmision from './../options/componentsDtun.js'
export default {
  name: 'ViewDtun',
  data() {
    return {
      logo: logTarifarito,
      showCard: false,
      components: componentesTransmision,
      values: [],
      actualiza: false
    }
  },
  computed: {
    ...mapGetters([
      'name',
      'roles'
    ])
  },
  created() {
    this.components.forEach(item => {
      item.data.forEach(campo => {
        // console.log('inputs transmisión: ', input)
        this.values[campo.input.key] = {
          placeholder: campo.input.placeholder,
          values: campo.input.value
        }
      })
    })
  },
  methods: {
    diferencia: function(key) {
      this.actualiza = false // sirve para renderizar el nuevo valor, no quitar
      const splitKey = key.split('_')
      const idKey = splitKey[0]
      const KeyOne = idKey + '_' + 1
      const KeyTwo = idKey + '_' + 2
      const KeyThree = idKey + '_' + 3
      const valor1 = this.values[KeyOne].values
      const valor2 = this.values[KeyTwo].values
      this.values[KeyThree].values = valor1 - valor2
      console.log('Values: ', this.values)
      this.actualiza = true
    },
    calcular: function() {
      this.showCard = true
    },
    verificar() {
      this.showCard = false
    },
    reportar() {
      this.showCard = false
      this.$alert('La empresa publico Dtun de una ADD diferente', 'TARIFARITO REPORTA', {
        confirmButtonText: 'Aceptar',
        callback: action => {
          this.$emit('clicked', false)
        }
      })
    }
  }
}
</script>

<style lang="scss">
  .el-collapse-item__content{
    padding-bottom: 1.5%;
  }
  .containerCards{
    border: 2px solid #C0C4CC;
    color: black;
    background-color: white;
    border-radius: 5px;
  }
  .contentConcept{
    border: 0px solid red;
    line-height: 2em;
    text-align: left;
    padding-left: 10%;
  }
  .contentText{
    border: 0px solid red;
    line-height: 3em;
    text-align: center;
  }
  .itemText{
    display:inline-block;
    vertical-align:middle;
    line-height:normal;
  }
</style>
