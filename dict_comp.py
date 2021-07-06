
def dict_comp(stop, step):
  #formula definition
  stop_step_div = stop//step
  stop = stop_step_div*step

  stop =range(1,stop+1)
  stop_step_div = range(1,stop_step_div +1)

  #forming dict keys
  key_former = [f"item - {i}" for i in (stop_step_div)]
  
  #forming dict values
  list3 = [i for i in stop]
  value_former = [list3[i:i+step] for i in range(0,len(list3),step)]

  #dict formed
  dict_formed = {key:value for key,value in zip(key_former,value_former)}

  return dict_formed


dict_comp(10,3)

