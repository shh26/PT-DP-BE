from django.db import models
from users.models import CustomUser

#Opportunity Model
class Opportunity(models.Model):

    
    class OpportunityStatus(models.TextChoices):
        Active='Active','Active'
        Converted='Converted','Converted'
        Planning='Planning','Planning'
        Revisit='Revisit','Revisit'
        Rejected='Rejected','Rejected'
        DRAFT = 'Draft', 'Draft'
    
    class DivisionStatus(models.TextChoices):
        VSS = 'VSS', 'VSS'
        VSC = 'VSC', 'VSC'

    name=models.CharField(max_length=150,null = True, blank = True)
    description=models.TextField(null = True, blank = True)
    #added_by=models.CharField(max_length=50,null = True, blank = True) 
    process_owner=models.CharField(max_length=150,null = True, blank = True) 
    strategy_alignment_score=models.CharField(max_length=150,null = True, blank = True) 
    financial_return_score=models.CharField(max_length=150,null = True, blank = True) 
    delivery_success_score=models.CharField(max_length=150,null = True, blank = True) 
    overall_score=models.CharField(max_length=150,null = True, blank = True) 
    sponsor=models.CharField(max_length=150,null = True, blank = True) 
    service_technology_center=models.JSONField(null=True, blank=True)
    estimated_capex_cost=models.CharField(max_length=150,null = True, blank = True) 
    estimated_opex_cost=models.CharField(max_length=150,null = True, blank = True) 
    business_benefit_value=models.TextField(null = True, blank = True) 
    current_pain_point_and_issue=models.TextField(null = True, blank = True) 
    forecast_customer_impact=models.TextField(null = True, blank = True) 
    estimated_hours=models.CharField(max_length=150,null = True, blank = True) 
    estimated_cost_saving=models.CharField(max_length=150,null = True, blank = True)
    estimated_revenue_generation=models.CharField(max_length=150,null = True, blank = True)
    created_by=models.ForeignKey(CustomUser,on_delete=models.CASCADE) 
    status=models.CharField(
        max_length=10,
        choices=OpportunityStatus.choices,
        default=OpportunityStatus.Active

    )
    division_type=models.CharField(
        max_length=10,
        choices=DivisionStatus.choices,
        default=DivisionStatus.VSS
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 
    
    def __str__(self):
        return self.name
    

    def save(self, *args, **kwargs):
        try:
            strategy_alignment_score = float(self.strategy_alignment_score) if self.strategy_alignment_score else 0
            financial_return_score = float(self.financial_return_score) if self.financial_return_score else 0
            delivery_success_score = float(self.delivery_success_score) if self.delivery_success_score else 0
            
            if strategy_alignment_score and financial_return_score and delivery_success_score:
                self.overall_score = str(int((strategy_alignment_score + financial_return_score + delivery_success_score) / 3))
        except ValueError:
            self.overall_score = "0"
            
        super().save(*args, **kwargs)


    class Meta:
        db_table = 'opportunity'



class OpportunityComment(models.Model):
    opportunity=models.ForeignKey(Opportunity,on_delete=models.CASCADE) 
    comment=models.TextField(null=True,blank=True)
    status=models.CharField(max_length=150,null = True, blank = True)
    created_by=models.ForeignKey(CustomUser,on_delete=models.CASCADE) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 
    
    def __str__(self):
        return self.oportunity
    
    class Meta:
        db_table = 'opportunity_comment'