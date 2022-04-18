<template>
  <div class="components-container" style="border: 0px solid red; margin: 0;">		
		<el-row>
			<el-col :span="24">
				<div style="border: 2px solid #C0C4CC; padding: 1%; padding-bottom: 0%;">
					<el-row>
						<el-col :span="2" style="border: 0px solid; color: black;">		
							<div>
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
				<div style="border: 2px solid #C0C4CC; color: black;">
					<el-row>
						<el-col :span="24" style="border: 0px solid; color: black; padding-top: 1%;">	
							<el-row>
								<el-col :span="12" style="border: 0px solid; color: black; text-align: left; padding-left: 2%;">									
									
								</el-col>
								<el-col :span="12" style="border: 0px solid; color: black; text-align: center; padding-right: 2%;">									
									
								</el-col>
							</el-row>
						</el-col>
					</el-row>
				</div>
			</el-col>
		</el-row>
  </div>
</template>

<script>
	import { mapGetters } from 'vuex'
	import BackToTop from '@/components/BackToTop'
	import logTarifarito from "../../../../../../assets/logo_buho.png"

  export default {
		name: 'viewG',
		components: { BackToTop },
		data() {
			return {
				logo: logTarifarito,
				myBackToTopStyle: {
					right: '50px',
					bottom: '50px',
					width: '40px',
					height: '40px',
					'border-radius': '4px',
					'line-height': '45px',
					background: '#e7eaf1'
				}    
			}
		},
		methods: {
			
		},
    computed: {
      ...mapGetters([
        'name',
        'roles'
      ])
    },
		created() {

		}
	}
</script>

<style lang="scss">
	
</style>