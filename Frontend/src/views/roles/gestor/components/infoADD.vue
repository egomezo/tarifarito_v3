<template>
  <div class="div-cont">
    <el-row class="cont-row">
      <el-col :span="24">
        <aside>
          <span class="text-header">
            <b>DIRECCIÓN TÉCNICA DE GESTIÓN DE ENERGÍA</b>
          </span>
        </aside>
      </el-col>
      <el-col :span="24">
        <aside>
          <span class="text-user">
            <b>{{ name }}</b>
          </span>
        </aside>
      </el-col>
    </el-row>

    <el-card class="box-card card-header">
      <div slot="header" class="clearfix">
        <span class="text-page">
          <b>INFORMACIÓN ÁREAS DE DISTRIBUCIÓN</b>
        </span>
      </div>
      <el-row :gutter="10">
        <el-col :sm="24" :md="24" style="text-align: center;">
          <el-select
            v-model="value1"
            filterable
            placeholder="Mercado"
            class="select-style"
            @change="verifyVariable($event)"
          >
            <el-option
              v-for="item in optionsMercado"
              :key="item.id_mercado"
              :label="`${item.id_mercado} - ${item.nom_mercado}`"
              :value="item.id_mercado"
            />
          </el-select>
        </el-col>
      </el-row>
    </el-card>

    <el-card class="box-card margin-card">
      <el-row class="cont-row">
        <el-col :sm="24" :md="24">
          <el-row class="cont-input">
            <el-col :sm="24" :md="24">
              <el-tooltip
                effect="dark"
                content="Corresponde al nombre del área de Distribución. 1= CENTRO. 2 = OCCIDENTE. 3 = ORIENTE. 4 = SUR."
                placement="top"
              >
                <i class="el-icon-info" style="color: #304156;" />
              </el-tooltip>
              <label>ADD</label>
            </el-col>
            <el-col :sm="24" :md="24" class="input-padding">
              <el-select v-model="valueADD" :disabled="disableSelect" placeholder="ADD" class="select" @change="verifyVariable('input_variable')">
                <el-option
                  v-for="add in optionsADD"
                  :key="add.value"
                  :label="add.label"
                  :value="add.value"
                />
              </el-select>
            </el-col>
          </el-row>
        </el-col>
      </el-row>

      <el-divider />

      <el-row :gutter="10">
        <el-col :sm="24" :md="12" class="cont-col-right">
          <el-button
            :disabled="disableModify"
            type="primary"
            icon="el-icon-refresh"
            :loading="loadingModify"
            class="btn"
            @click.native.prevent="modifyVariable"
          >Modificar</el-button>
        </el-col>
        <el-col :sm="24" :md="12">
          <el-button
            :disabled="disableLoad"
            type="success"
            icon="el-icon-check"
            :loading="loadingLoad"
            class="btn"
            @click.native.prevent="saveVariable"
          >Cargar</el-button>
        </el-col>
      </el-row>
    </el-card>

    <!-- you can add element-ui's tooltip -->
    <el-tooltip placement="top" content="subir">
      <back-to-top
        :custom-style="myBackToTopStyle"
        :visibility-height="300"
        :back-position="50"
        transition-name="fade"
      />
    </el-tooltip>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import BackToTop from '@/components/BackToTop'
import { Message } from 'element-ui'
import { CONSTANTS } from '../../../../constants/constants'
import {
  getInfoADDList,
  getInfoADD,
  putInfoADD,
  postInfoADD
} from '@/api/tarifarito/gestor/InfoADD'
import { getSUIMercadosList } from '@/api/tarifarito/sui-mercados'

export default {
  name: 'ViewInfoADD',
  components: { BackToTop },
  data() {
    this.getMercadosList()
    return {
      disableLoad: true,
      disableModify: true,
      disableVariable: true,
      disableSelect: true,
      loadingLoad: false,
      loadingModify: false,
      dialogFormVisible: false,
      dialogVisible: false,
      myBackToTopStyle: CONSTANTS.myBackToTopStyle,
      optionsMercado: [],
      value1: '',
      date: new Date(),
      optionsADD: CONSTANTS.optionsADD,
      valueADD: '',
      model: {}
    }
  },
  computed: {
    ...mapGetters(['name', 'roles'])
  },
  methods: {
    async getMercadosList() {
      await getSUIMercadosList().then(response => {
        // console.log(response)
        this.optionsMercado = JSON.parse(JSON.stringify(response))
      })
    },
    async verifyVariable(evt) {
      const mercado = this.value1
      await getInfoADD(mercado).then(response => {
        this.disableSelect = false
        if (response) {
          if (evt !== 'input_variable') {
            // console.log('Response: ', response)
            this.valueADD = response[0].add
            this.disableLoad = true
            this.disableModify = false
          } else {
            this.disableModify = false
          }
        } else {
          if (evt !== 'input_variable') {
            this.valueADD = ''
            this.disableLoad = true
            this.disableModify = true
          } else {
            this.disableLoad = false
          }
        }
      })
    },
    async modifyVariable() {
      this.loadingModify = true
      const mercado = this.value1
      const model = {
        usuario: this.name,
        fecha_modif: this.date,
        add: this.valueADD
      }
      await putInfoADD(mercado, model).then(response => {
        Message({
          message: 'Registros actualizados con éxito!',
          type: 'success',
          duration: 2 * 1000
        })
        this.disableModify = true
        this.loadingModify = false
      })
    },
    async saveVariable() {
      this.loadingLoad = true
      const mercado = this.value1
      await getInfoADDList().then(async response => {
        // Si ya existe el documento lo actualiza
        if (response.length !== 0) {
          const model = {
            usuario: this.name,
            fecha_modif: this.date,
            add: this.valueADD
          }
          await putInfoADD(mercado, model).then(response => {
            Message({
              message: 'Registros guardados con éxito!',
              type: 'success',
              duration: 2 * 1000
            })
          })
          this.loadingLoad = false
          this.disableLoad = true
        } else {
          // Si no existe el documento lo crea
          const model = {
            key: 0,
            mercados: {
              [`m_${mercado}`]: [
                {
                  usuario: this.name,
                  fecha_modif: this.date,
                  add: this.valueADD
                }
              ]
            }
          }
          await postInfoADD(model).then(response => {
            this.loadingLoad = false
            this.disableLoad = true
            Message({
              message: 'Registros guardados con éxito!',
              type: 'success',
              duration: 2 * 1000
            })
          })
        }
      })
    }
  }
}
</script>

<style lang="scss">
	.text-header {
		color: black;
	}

	.margin-card {
		margin-top: 1em;
	}

	.cont-row {
		text-align: center;
	}

	.input-padding {
		padding-top: 0.5em;
	}

	.dialog-style {
		border: 1px solid red;
	}

  .dialog-class {
    border-radius: 10px;
  }

  .dialog-class .el-dialog__header {
    border-radius: 10px 10px 0px 0px;
  }

  .card-header .el-card__header {
    background: #F2F6FC;
  }

	// Pantallas superiores a 800px (PC)
	@media screen and (min-width: 800px) {
    .div-cont {
      padding-top: 1.5em;
      padding-left: 3em;
      padding-right: 3em;
    }

		.text-header {
			font-size: x-large;
		}

		.text-user {
			font-size: large;
		}

		.text-page {
			font-size: medium;
		}

		.cont-col-right {
			text-align: right;
		}

		.select {
			width: 13em;
		}

		.input-number {
			width: 17em;
		}

		.btn {
			width: 10em;
		}

		.cont-input {
			padding-top: 1.5em;
			padding-bottom: 1.5em;
		}

		.input-select {
			width: 13em;
		}

    .select-style {
      width: 13em;
    }
	}

	// Pantallas inferiores a 800px (mobile)
	@media screen and (max-width: 800px) {
    .div-cont {
      padding: 1em;
    }

		.text-header {
			font-size: small;
		}

		.text-user {
			font-size: small;
		}

		.text-page {
			font-size: small;
		}

		.cont-col-right {
			padding-bottom: 0.5em;
		}

		.select {
			width: 100%;
		}

		.input-number {
			width: 100%;
		}

		.btn {
			width: 100%;
		}

		.cont-input {
			padding-top: 1em;
		}

		.input-select {
			width: 77%;
		}

		.btn-plain {
			width: 21%;
		}

    .select-style {
      width: 100%;
    }

    .select-popper {
      li {
        font-size: 0.45em;
      }
    }
	}
</style>
