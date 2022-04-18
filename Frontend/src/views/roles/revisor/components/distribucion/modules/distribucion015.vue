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
                  </aside>
                </el-col>
              </el-row>
            </el-col>
          </el-row>
        </div>
        <br>
        <div style="border: 2px solid #C0C4CC; color: black; overflow-y:scroll; height: 43em; background-color: white; border-radius: 5px;"> <!-- valor pantalla super -->
          <el-row>
            <el-col :span="24" style="border: 0px solid; color: black; padding: 1%;">
              <el-card class="box-card" style="padding-left: 2em; padding-right: 2em; margin-bottom: 1em;">
                <el-row style="font-weight: bold; padding-bottom: 1%; text-align: center;">
                  <el-col style="border: 0px solid red; text-align: left;" :span="13">
                    <span>CONCEPTO</span> <span style="color: white;">{{ actualiza }}</span> <!-- No borrar el span, este componente permite renderizar la diferencia de valores -->
                  </el-col>
                  <el-col style="border: 0px solid red;" :span="2">
                    <span>UNIDAD</span>
                  </el-col>
                  <el-col style="border: 0px solid red;" :span="3">
                    <span>VALORES</span>
                  </el-col>
                  <el-col style="border: 0px solid red;" :span="3">
                    <span>VALORES</span>
                  </el-col>
                  <el-col style="border: 0px solid red;" :span="3">
                    <span>DIFERENCIA</span>
                  </el-col>
                </el-row>
                <el-row>
                  <el-col :span="24">
                    <el-collapse accordion>
                      <el-collapse-item v-for="item in components" :key="item.title" :name="item.name">
                        <template slot="title">
                          {{ item.title }}<i class="header-icon el-icon-information" />
                        </template>
                        <el-row v-for="value in item.data" :key="value.campo">
                          <el-col :span="13" style="padding-left: 2%; border: 0px solid blue;">
                            <span>{{ value.concepto }}</span>
                          </el-col>
                          <el-col style="border: 0px solid blue; text-align: center;" :span="2">
                            <span>{{ value.unidad }}</span>
                          </el-col>
                          <span v-for="valorInput in value.inputs" :key="valorInput.key">
                            <span v-if="valorInput.start === true && valorInput.diferencia === false">
                              <el-col v-if="valorInputDefault === valorInput.show" style="border: 0px solid yellow; text-align: center;" :span="3">
                                <input
                                  v-model="values[valorInput.key].values"
                                  :type="valorInput.type"
                                  :placeholder="valorInput.placeholder"
                                  style="width: 95%; height: 2em; margin-bottom: 0.5em;"
                                  :disabled="true"
                                  @input="diferencia(valorInput.key)"
                                >
                              </el-col>
                            </span>
                            <span v-else-if="valorInput.start === false && valorInput.diferencia === false">
                              <el-col v-if="valoresDiferencia === valorInput.show" style="border: 0px solid blue;" :span="3">
                                <input
                                  v-model="values[valorInput.key].values"
                                  :type="valorInput.type"
                                  :placeholder="valorInput.placeholder"
                                  style="width: 95%; height: 2em; margin-bottom: 0.5em;"
                                  @input="diferencia(valorInput.key)"
                                >
                              </el-col>
                            </span>
                            <span v-else>
                              <el-col v-if="valoresDiferencia === valorInput.show" style="border: 0px solid red;" :span="3">
                                <input
                                  v-model="values[valorInput.key].values"
                                  :type="valorInput.type"
                                  :placeholder="valorInput.placeholder"
                                  :disabled="true"
                                  style="width: 95%; height: 2em; margin-bottom: 0.5em;"
                                >
                              </el-col>
                            </span>
                          </span>
                        </el-row>
                      </el-collapse-item>
                    </el-collapse>
                  </el-col>
                </el-row>
              </el-card>
            </el-col>
          </el-row>
        </div>
      </el-col>
    </el-row>
    <el-row style="padding-top: 1%;">
      <el-col :span="12" style="border: 0px solid yellow;">
        <span>Fórmula componente</span>
        <el-tooltip class="item" effect="dark" content="Fórmula" placement="top-start">
          <i class="el-icon-info" style="color: #304156;" />
        </el-tooltip>
      </el-col>
      <el-col :span="12" style="text-align: right; border: 0px solid;">
        <el-button type="primary" @click="calcular">Calcular</el-button>
        <el-button v-if="!valoresDiferencia" type="primary" @click="verificar">Verificado</el-button>
        <el-button v-if="valoresDiferencia" type="primary" @click="reportar">Reportar</el-button>
      </el-col>
      <el-col style="border: 0px solid red; padding-top: 1em;" :span="24">
        <!-- <el-card style="padding-bottom: 0.5em;"> -->
        <el-card class="box-card" style="border: 2px solid #C0C4CC;">
          <div slot="header">
            <span><b>Publicación LAC | $/kWh</b></span>
          </div>
          <el-row style="padding-top: 0.5em; padding-left: 5em;">
            <span v-for="item in componentsFooter" :key="item.name">
              <el-col :span="12" style="padding-bottom: 1em; border: 0px solid blue;">
                <el-row>
                  <el-col class="contentText" :span="15" style="border: 0px solid blue;">
                    <span>{{ item.concepto }}</span>
                  </el-col>
                  <el-col :span="9" style="border: 0px solid red;">
                    <input
                      v-model="valuesFooter[item.input.key].values"
                      :type="item.input.type"
                      style="width: 30%;"
                    >
                  </el-col>
                </el-row>
              </el-col>
            </span>
          </el-row>
        </el-card>
      </el-col>
    </el-row>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import logTarifarito from '../../../../../../assets/logo_buho.png'
import distribucion015 from './../options/distribucion015'
import ComponentesFooter from './../options/componentD015Footer'

export default {
  name: 'D015',
  data() {
    return {
      logo: logTarifarito,
      valorInputDefault: true,
      valoresDiferencia: false,
      components: distribucion015,
      input: 0,
      values: [],
      actualiza: false,
      componentsFooter: ComponentesFooter,
      valuesFooter: []
    }
  },
  computed: {
    ...mapGetters([
      'name',
      'roles'
    ])
  },
  created() {
    const valores = []
    let diferencia = 0
    this.components.forEach(item => {
      item.data.forEach(input => {
        input.inputs.forEach(campo => {
          if (campo.diferencia === false) {
            valores.push(campo.value)
            this.values[campo.key] = {
              placeholder: campo.placeholder,
              show: campo.show,
              values: campo.value
            }
          } else {
            diferencia = valores[0] - valores[1]
            this.values[campo.key] = {
              placeholder: campo.placeholder,
              show: campo.show,
              values: diferencia
            }
          }
        })
      })
    })
    this.componentsFooter.forEach(item => {
      this.valuesFooter[item.input.key] = {
        placeholder: item.input.placeholder,
        values: item.input.value
      }
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
      this.valoresDiferencia = true
    },
    verificar() {
      this.valoresDiferencia = false
    },
    reportar() {
      this.valoresDiferencia = false
      this.$alert('<p style="text-align: center;">La empresa publico el cargo máximo y no el cargo minimo</p>', 'TARIFARITO REPORTA', {
        dangerouslyUseHTMLString: true,
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

  .contentText{
    line-height: 1.5em;
    text-align: left;
  }
</style>
